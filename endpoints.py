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


if __name__ == "__main__":
    app.run(debug=True)

