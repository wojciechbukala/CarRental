import db_connection as db_conn
from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)

