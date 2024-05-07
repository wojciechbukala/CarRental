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
    db.cursor.execute(f"SELECT * FROM public.\"Customer\"")
    customer = db.cursor.fetchall()
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
        \"AddressID\", \"Address1\", \"Address2\", \"PostalCode\", \"City\", \"Country\", \"PhoneNumber\")
        VALUES ({address_id}, \'{address1}\', \'{address2}\', \'{postal_code}\', \'{city}\', \'{country}\', \'{phone_number}\');""")

    db.conn.commit()

    return jsonify({"message": "Address added successfully"})

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
        \"CarID\", \"Brand\", \"YearOfProduction\", \"Color\", \"Insurance\", \"Diagnostics\", \"SegmentID\")
        VALUES ({car_id}, \'{brand}\', {year_of_production}, \'{color}\', {insurance}, {diagnostics}, {segment_id});""")

    db.conn.commit()

    return jsonify({"message": "Car added successfully"})

@app.route("/add_customer", methods=["POST"])
def add_car():
    data = request.json
    customer_id = data.get("CustomerID")
    first_name = data.get("FirstName")
    last_name = data.get("LastName")
    email = data.get("Email")
    address_id = data.get("AddressID")
    create_date = data.get("CreateDate")

    db.cursor.execute(f"""INSERT INTO public.\"Customer\"(
        \"CustomerID\", \"FirstName\", \"LastName\", \"Email\", \"AddressID\", \"CreateDate\")
        VALUES ({customer_id}, \'{first_name}\', {last_name}, \'{email}\', {address_id}, {create_date});""")

    db.conn.commit()

    return jsonify({"message": "Customer added successfully"})

if __name__ == "__main__":
    app.run(debug=True)

