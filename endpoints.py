import db_connection as db_conn
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

db = db_conn.Database(dbname = "CarRental", user = "postgres", password = "postgres_pass")


@app.route("/address", methods=["GET"])
def get_addresses():
    db.cursor.execute(f"SELECT * FROM public.\"Address\"")
    addresses = db.cursor.fetchall()
    return jsonify(addresses)

@app.route("/car", methods=["GET"])
def get_cars():
    db.cursor.execute(f"SELECT * FROM public.\"Car\"")
    cars = db.cursor.fetchall()
    return jsonify(cars)

@app.route("/get_car_by_model", methods=["GET"])
def get_car_by_model():
    brand = request.args.get("brand")
    model = request.args.get("model")
    db.cursor.execute(f"""SELECT * FROM public.\"Car\" 
    WHERE \"Brand\" = \'{brand}\' AND \"Model\" = \'{model}\' 
    LIMIT 1;""")
    cars = db.cursor.fetchone()
    return jsonify(cars)

# @app.route("/get_available_cars", methods=["GET"])
# def get_available_cars():
#     db.cursor.execute("""SELECT \"Model\", \"Brand\" FROM public.\"Car\"
#     WHERE \"Insurance\" <> \'False\' AND \"Diagnostics\" <> \'False\'""")
#     cars = db.cursor.fetchall()
#     return jsonify(cars)

@app.route("/get_available_cars", methods=["GET"])
def get_available_cars():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    db.cursor.execute(f"""SELECT \"Model\", \"Brand\" FROM public.\"Car\"
    WHERE (\"Insurance\" <> \'False\' AND \"Diagnostics\" <> \'False\')
    AND \"CarID\" NOT IN (SELECT \"CarID\" FROM public.\"Rental\"
    WHERE (\"RentalDate\" <= \'{end_date}\' AND \"ReturnDate\" >= \'{start_date}\')
    OR (\"RentalDate\" <= \'{start_date}\' AND \"ReturnDate\" >= \'{start_date}\')
    OR (\"RentalDate\" >= \'{start_date}\' AND \"ReturnDate\" <= \'{end_date}\'))""")
    cars = db.cursor.fetchall()
    return jsonify(cars)

@app.route("/customer", methods=["GET"])
def get_customer():
    email = request.args.get("email", default="%")
    password = request.args.get("password", default="%")
    db.cursor.execute(f"""SELECT * FROM public.\"Customer\"
        WHERE \"Email\" LIKE \'{email}\' AND \"Password\" LIKE \'{password}\'""")
    customer = db.cursor.fetchall()

    if not customer:  # Jeśli nie znaleziono customera
        return jsonify({"message": "No customer found with the specified email"}), 404
    
    return jsonify(customer)

@app.route("/payment", methods=["GET"])
def get_payment():
    db.cursor.execute(f"SELECT * FROM public.\"Payment\"")
    payment = db.cursor.fetchall()
    return jsonify(payment)

@app.route("/rental", methods=["GET"])
def get_rental():
    db.cursor.execute(f"SELECT * FROM public.\"Rental\"")
    rental = db.cursor.fetchall()
    return jsonify(rental)

@app.route("/rental_all", methods=["GET"])
def get_all_rentals():
    db.cursor.execute(f"""SELECT \"RentalID\", \"RentalDate\", \"ReturnDate\",
    \"FirstName\", \"LastName\", \"Brand\", \"Model\"
    FROM public.\"Rental\"
    LEFT JOIN \"Customer\" ON \"Rental\".\"CustomerID\" = \"Customer\".\"CustomerID\"
    LEFT JOIN \"Car\" ON \"Rental\".\"CarID\" = \"Car\".\"CarID\"""")
    rental = db.cursor.fetchall()
    return jsonify(rental)

@app.route("/rental_by_customer_id", methods=["GET"])
def get_rental_by_cutomer_id():
    customer_id = request.args.get("customer_id")
    db.cursor.execute(f"""SELECT \"RentalDate\", \"ReturnDate\", \"Brand\", \"Model\"
	FROM public.\"Rental\"
	LEFT JOIN public.\"Car\" ON \"Car\".\"CarID\" = \"Rental\".\"CarID\" 
    WHERE \"CustomerID\"={customer_id}""")
    rental = db.cursor.fetchall()
    return jsonify(rental)

@app.route("/segment", methods=["GET"])
def get_segment():
    db.cursor.execute(f"SELECT * FROM public.\"Segment\"")
    segment = db.cursor.fetchall()
    return jsonify(segment)

@app.route("/staff", methods=["GET"])
def get_staff():
    db.cursor.execute(f"SELECT * FROM public.\"Staff\"")
    staff = db.cursor.fetchall()
    return jsonify(staff)

@app.route("/add_address", methods=["POST"])
def add_address():
    data = request.json
    address_id = data.get("AddressID")
    address1 = data.get("Address1")
    address2 = data.get("Address2")
    postal_code = data.get("PostalCode")
    city = data.get("City")
    country = data.get("Country")
    phone_number = data.get("PhoneNumber")

    db.cursor.execute(f"""INSERT INTO public.\"Address\"(
        \"Address1\", \"Address2\", \"PostalCode\", \"City\", \"Country\", \"PhoneNumber\")
        VALUES (\'{address1}\', \'{address2}\', \'{postal_code}\', \'{city}\', \'{country}\', \'{phone_number}\')
        RETURNING \"AddressID\";""")
    
    new_id = db.cursor.fetchone()[0]

    db.conn.commit()

    return jsonify({"message": "Address added successfully", "AddressID": new_id})

@app.route("/add_car", methods=["POST"])
def add_car():
    data = request.json
    car_id = data.get("CarID")
    brand = data.get("Brand")
    year_of_production = data.get("YearOfProduction")
    color = data.get("Color")
    insurance = data.get("Insurance")
    dignostics = data.get("Diagnostics")
    segment_id = data.get("SegmanetID")

    db.cursor.execute(f"""INSERT INTO public.\"Car\"(
        \"Brand\", \"YearOfProduction\", \"Color\", \"Insurance\", \"Diagnostics\", \"SegmentID\")
        VALUES (\'{brand}\', {year_of_production}, \'{color}\', {insurance}, {diagnostics}, {segment_id});""")

    db.conn.commit()

    return jsonify({"message": "Car added successfully"})

@app.route("/add_customer", methods=["POST"])
def add_customer():
    data = request.json
    customer_id = data.get("CustomerID")
    first_name = data.get("FirstName")
    last_name = data.get("LastName")
    email = data.get("Email")
    password = data.get("Password")
    address_id = data.get("AddressID")
    create_date = data.get("CreateDate")

    db.cursor.execute(f"""INSERT INTO public.\"Customer\"(
        \"FirstName\", \"LastName\", \"Email\", \"Password\", \"CreateDate\")
        VALUES (\'{first_name}\', \'{last_name}\', \'{email}\', \'{password}\', \'{create_date}\');""")

    db.conn.commit()

    return jsonify({"message": "Customer  added successfully"})

@app.route("/add_customer_address", methods=["POST"])
def add_customer_address():
    data = request.json
    address_id = data.get("AddressID")
    customer_id = request.args.get("customer_id")

    db.cursor.execute(f"UPDATE public.\"Customer\" SET \"AddressID\" = {address_id} WHERE \"CustomerID\" = {customer_id}")

    db.conn.commit()

    return jsonify({"message": "AddressID upadated"})

@app.route("/add_new_rental", methods=["POST"])
def add_new_rental():
    data = request.json

    rental_date = data.get("RentalDate")
    return_date = data.get("ReturnDate")
    car_id = data.get("CarID")
    customer_id = data.get("CustomerID")

    db.cursor.execute(f"""INSERT INTO public.\"Rental\"(
	\"RentalDate\", \"ReturnDate\", \"CarID\", \"CustomerID\")
	VALUES (\'{rental_date}\', \'{return_date}\', {car_id}, {customer_id});""")

    db.conn.commit()

    return jsonify({"message": "New rental added"})

@app.route("/update_insurance", methods=["POST"])
def update_insurance():
    new_status = request.args.get("new_status", default="True")
    car_id = request.args.get("car_id")

    db.cursor.execute(f"UPDATE public.\"Car\" SET \"Insurance\" = \'{new_status}\' WHERE \"CarID\" = {car_id}")

    db.conn.commit()

    return jsonify({"message": "Insurance status updated"})

@app.route("/update_diagnostics", methods=["POST"])
def update_diagnostics():
    new_status = request.args.get("new_status", default="True")
    car_id = request.args.get("car_id")

    db.cursor.execute(f"UPDATE public.\"Car\" SET \"Diagnostics\" = \'{new_status}\' WHERE \"CarID\" = {car_id}")

    db.conn.commit()

    return jsonify({"message": "Diagnostics status updated"})

if __name__ == "__main__":
    app.run(debug=True)


