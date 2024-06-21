import db_connection as db_conn
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

#db = db_conn.Database(dbname = "CarRental", user = "postgres", password = "postgres_pass")

#connection with master
db_m = db_conn.Database(dbname = "postgresdb", user = "postgresadmin", password = "admin123", port=5001)

#connection with slave
db_s = db_conn.Database(dbname = "postgresdb", user = "postgresadmin", password = "admin123", port=5002)


@app.route("/address", methods=["GET"])
def get_addresses():
    db_s.cursor.execute(f"SELECT * FROM public.\"Address\"")
    addresses = db_s.cursor.fetchall()
    return jsonify(addresses)

@app.route("/car", methods=["GET"])
def get_cars():
    db_s.cursor.execute(f"SELECT * FROM public.\"Car\"")
    cars = db_s.cursor.fetchall()
    return jsonify(cars)

@app.route("/get_car_by_model", methods=["GET"])
def get_car_by_model():
    brand = request.args.get("brand")
    model = request.args.get("model")
    db_s.cursor.execute(f"""SELECT * FROM public.\"Car\" 
    WHERE \"Brand\" = \'{brand}\' AND \"Model\" = \'{model}\' 
    LIMIT 1;""")
    cars = db_s.cursor.fetchone()
    return jsonify(cars)

@app.route("/cars_by_id", methods=["GET"])
def get_cars_by_id():
    id = request.args.get("id")
    db_s.cursor.execute(f"""SELECT *
    FROM public.\"Car\"
    WHERE \"CarID\" = {id}""")
    cars = db_s.cursor.fetchall()
    return jsonify(cars)

@app.route("/get_available_cars", methods=["GET"])
def get_available_cars():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    segment = request.args.get("segment")
    car_brand = request.args.get("car_brand")
    car_model = request.args.get("car_model")


    query = """SELECT \"CarID\", \"Model\", \"Brand\", \"YearOfProduction\", \"PricePerHour\"
    FROM public.\"Car\"
    LEFT JOIN \"Segment\" ON \"Segment\".\"SegmentID\" = \"Car\".\"SegmentID\"
    WHERE (\"Insurance\" <> \'False\' AND \"Diagnostics\" <> \'False\')
    AND \"CarID\" NOT IN (
        SELECT \"CarID\" FROM public.\"Rental\"
        WHERE (%s <= "ReturnDate" AND %s >= "RentalDate")
    )"""

    parameters = [start_date, end_date]

    if segment:
        query += ' AND "Segment"."SegmentSign" = %s'
        parameters.append(segment)
    if car_brand:
        query += ' AND "Brand" = %s'
        parameters.append(car_brand)
    if car_model:
        query += ' AND "Model" = %s'
        parameters.append(car_model)

    db_s.cursor.execute(query, parameters)

    cars = db_s.cursor.fetchall()
    return jsonify(cars)

@app.route("/customer", methods=["GET"])
def get_customer():
    email = request.args.get("email", default="%")
    password = request.args.get("password", default="%")
    db_s.cursor.execute(f"""SELECT * FROM public.\"Customer\"
        WHERE \"Email\" LIKE \'{email}\' AND \"Password\" LIKE \'{password}\'""")
    customer = db_s.cursor.fetchall()

    if not customer:  # Jeśli nie znaleziono customera
        return jsonify({"message": "No customer found with the specified email"}), 404
    
    return jsonify(customer)

@app.route("/login_staff", methods=["GET"])
def login_staff():
    email = request.args.get("email", default="%")
    db_s.cursor.execute(f"""SELECT * FROM public.\"Staff\"
        WHERE \"Email\" LIKE \'{email}\'""")
    staff = db_s.cursor.fetchall()

    if not staff:  # Jeśli nie znaleziono pracownika
        return jsonify({"message": "No staff found with the specified email"}), 404
    
    return jsonify(staff)

@app.route("/get_customers", methods=["GET"])
def get_customers():
    db_s.cursor.execute(f"""SELECT \"FirstName\", \"LastName\", \"Email\", 
    \"Address\".\"Address1\", \"Address\".\"Address2\", \"Address\".\"PostalCode\", \"Address\".\"City\"
    FROM public.\"Customer\"
    LEFT JOIN public.\"Address\" ON \"Customer\".\"AddressID\" = \"Address\".\"AddressID\"""")
    customers = db_s.cursor.fetchall()
    return jsonify(customers)

@app.route("/payment", methods=["GET"])
def get_payment():
    db_s.cursor.execute(f"SELECT * FROM public.\"Payment\"")
    payment = db_s.cursor.fetchall()
    return jsonify(payment)

@app.route("/rental", methods=["GET"])
def get_rental():
    db_s.cursor.execute(f"SELECT * FROM public.\"Rental\"")
    rental = db_s.cursor.fetchall()
    return jsonify(rental)

@app.route("/rental_all", methods=["GET"])
def get_all_rentals():
    db_s.cursor.execute(f"""SELECT \"RentalID\", \"RentalDate\", \"ReturnDate\", \"Rental\".\"CarID\",
    \"Brand\", \"Model\", \"Rental\".\"CustomerID\", \"FirstName\", \"LastName\"
    FROM public.\"Rental\"
    LEFT JOIN \"Customer\" ON \"Rental\".\"CustomerID\" = \"Customer\".\"CustomerID\"
    LEFT JOIN \"Car\" ON \"Rental\".\"CarID\" = \"Car\".\"CarID\"""")
    rental = db_s.cursor.fetchall()
    return jsonify(rental)

@app.route("/rental_by_customer_id", methods=["GET"])
def get_rental_by_cutomer_id():
    customer_id = request.args.get("customer_id")
    db_s.cursor.execute(f"""SELECT \"RentalDate\", \"ReturnDate\", \"Brand\", \"Model\"
	FROM public.\"Rental\"
	LEFT JOIN public.\"Car\" ON \"Car\".\"CarID\" = \"Rental\".\"CarID\" 
    WHERE \"CustomerID\"={customer_id}""")
    rental = db_s.cursor.fetchall()
    return jsonify(rental)

@app.route("/segment", methods=["GET"])
def get_segment():
    db_s.cursor.execute(f"SELECT * FROM public.\"Segment\"")
    segment = db_s.cursor.fetchall()
    return jsonify(segment)

@app.route("/staff", methods=["GET"])
def get_staff():
    db_s.cursor.execute(f"SELECT \"FirstName\", \"LastName\", \"Email\" FROM public.\"Staff\"")
    staff = db_s.cursor.fetchall()
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

    db_m.cursor.execute(f"""INSERT INTO public.\"Address\"(
        \"Address1\", \"Address2\", \"PostalCode\", \"City\", \"Country\", \"PhoneNumber\")
        VALUES (\'{address1}\', \'{address2}\', \'{postal_code}\', \'{city}\', \'{country}\', \'{phone_number}\')
        RETURNING \"AddressID\";""")
    
    new_id = db_m.cursor.fetchone()[0]

    db_m.conn.commit()

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

    db_m.cursor.execute(f"""INSERT INTO public.\"Car\"(
        \"Brand\", \"YearOfProduction\", \"Color\", \"Insurance\", \"Diagnostics\", \"SegmentID\")
        VALUES (\'{brand}\', {year_of_production}, \'{color}\', {insurance}, {diagnostics}, {segment_id});""")

    db_m.conn.commit()

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

    db_m.cursor.execute(f"""INSERT INTO public.\"Customer\"(
        \"FirstName\", \"LastName\", \"Email\", \"Password\", \"CreateDate\")
        VALUES (\'{first_name}\', \'{last_name}\', \'{email}\', \'{password}\', \'{create_date}\');""")

    db_m.conn.commit()

    return jsonify({"message": "Customer  added successfully"})

@app.route("/add_customer_address", methods=["POST"])
def add_customer_address():
    data = request.json
    address_id = data.get("AddressID")
    customer_id = request.args.get("customer_id")

    db_m.cursor.execute(f"UPDATE public.\"Customer\" SET \"AddressID\" = {address_id} WHERE \"CustomerID\" = {customer_id}")

    db_m.conn.commit()

    return jsonify({"message": "AddressID upadated"})

# transakacja wypożyczenia
@app.route("/rent_a_car", methods=["POST"])
def rent_a_car():
    data = request.json
    car_id = data.get("CarID")
    user_id = data.get("UserID")
    start_date = data.get("StartDate")
    end_date = data.get("EndDate")

    try:
        db_m.cursor.execute("BEGIN;")

        db_m.cursor.execute(f"SELECT \"Status\" FROM public.\"Car\" WHERE \"CarID\" = {car_id};")

        car_status = db_m.cursor.fetchone()[0]

        if car_status != 'available':
            raise Exception("Car is not available")

        db_m.cursor.execute(f"UPDATE public.\"Car\" SET \"Status\" = 'rented' WHERE \"CarID\" = {car_id};")

        db_m.cursor.execute(f"""INSERT INTO public.\"Rental\"(
        \"RentalDate\", \"ReturnDate\", \"CarID\", \"CustomerID\")
        VALUES (\'{start_date}\', \'{end_date}\', {car_id}, {user_id});""")

        db_m.conn.commit()

        return jsonify({"message": "Car rented successfully", "CarID": car_id}), 200

    except Exception as e:
        db_m.conn.rollback()
        return jsonify({"message": str(e)}), 500


# transakacja zwrotu
@app.route("/return_a_car", methods=["POST"])
def return_a_car():
    data = request.json
    car_id = data.get("CarID")

    try:
        db_m.cursor.execute("BEGIN;")

        db_m.cursor.execute(f"SELECT \"Status\" FROM public.\"Car\" WHERE \"CarID\" = {car_id};")

        car_status = db_m.cursor.fetchone()[0]

        if car_status != 'rented':
            raise Exception("Car is not rented")

        db_m.cursor.execute(f"UPDATE public.\"Car\" SET \"Status\" = 'available' WHERE \"CarID\" = {car_id};")

        db_m.cursor.execute(f"""DELETE FROM public.\"Rental\" WHERE \"CarID\" = {car_id};""")

        db_m.conn.commit()

        return jsonify({"message": "Car returned successfully", "CarID": car_id}), 200

    except Exception as e:
        db_m.conn.rollback()
        return jsonify({"message": str(e)}), 500

@app.route("/add_new_rental", methods=["POST"])
def add_new_rental():
    data = request.json

    rental_date = data.get("RentalDate")
    return_date = data.get("ReturnDate")
    car_id = data.get("CarID")
    customer_id = data.get("CustomerID")

    db_m.cursor.execute(f"""INSERT INTO public.\"Rental\"(
	\"RentalDate\", \"ReturnDate\", \"CarID\", \"CustomerID\")
	VALUES (\'{rental_date}\', \'{return_date}\', {car_id}, {customer_id});""")

    db_m.conn.commit()

    return jsonify({"message": "New rental added"})

@app.route("/update_insurance", methods=["POST"])
def update_insurance():
    new_status = request.args.get("new_status", default="True")
    car_id = request.args.get("car_id")

    db_m.cursor.execute(f"UPDATE public.\"Car\" SET \"Insurance\" = \'{new_status}\' WHERE \"CarID\" = {car_id}")

    db_m.conn.commit()

    return jsonify({"message": "Insurance status updated"})

@app.route("/update_diagnostics", methods=["POST"])
def update_diagnostics():
    new_status = request.args.get("new_status", default="True")
    car_id = request.args.get("car_id")

    db_m.cursor.execute(f"UPDATE public.\"Car\" SET \"Diagnostics\" = \'{new_status}\' WHERE \"CarID\" = {car_id}")

    db_m.conn.commit()

    return jsonify({"message": "Diagnostics status updated"})

@app.route("/update_status", methods=["POST"])
def update_status():
    new_status = request.args.get("new_status", default="True")
    car_id = request.args.get("car_id")

    db_m.cursor.execute(f"UPDATE public.\"Car\" SET \"Status\" = \'{new_status}\' WHERE \"CarID\" = {car_id}")

    db_m.conn.commit()

    return jsonify({"message": "Status updated"})

if __name__ == "__main__":
    app.run(debug=True)


