import endpoints
import requests
from datetime import date

def md5(password):
    pass

def get_customer_by_email(email):
    url = f"http://127.0.0.1:5000/customer?email={email}"
    response = requests.get(url)

    if response.status_code == 200:
        customer = response.json()
        return [True, customer]
    else:
        error_message = response.json()["message"]
        return [False, error_message]

def register(first_name, last_name, email, password):
   
    if get_customer_by_email(email)[0] == True:
        print("User already exists")
    
    elif "@" not in email:
        print("Please type valid email")

    else:
        url_customer = 'http://127.0.0.1:5000/add_customer'
        data_customer = {
            "FirstName": f"{first_name}",
            "LastName": f"{last_name}",
            "Email": f"{email}",
            "Password": f"{password}",
            "CreateDate": f"{date.today()}"
        }
        response = requests.post(url_customer, json = data_customer)

def login(email, password):
    url = f"http://127.0.0.1:5000/customer?email={email}&password={password}"
    response = requests.get(url)

    if response.status_code == 200:
        print("You are logged in")
    else:
        print("Error")

def rent_a_car():
    pass

login("wojciech_bukala@outlook.com", "wojtek123")
#register("piotr", "omiecina", "piotr.omiecina@gmail.com", "piotr123")
