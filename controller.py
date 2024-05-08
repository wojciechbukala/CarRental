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
        user_email = email
    else:
        print("Error")

def register_new_car():
    url_car = 'http://127.0.0.1:5000/add_car'

def register_address(email, address1, address2, postal_code, city, country, phone_number):
    
    customer_id = get_customer_by_email(email)[1][0][0]
    print(customer_id)
    
    data_address = {
        "Address1": f"{address1}",
        "Address2": f"{address2}",
        "PostalCode": f"{postal_code}",
        "City": f"{city}",
        "Country": f"{country}",
        "PhoneNumber" : f"{phone_number}"
    }
    url_address = 'http://127.0.0.1:5000/add_address'
    response1 = requests.post(url_address, json = data_address)

    if response1.status_code == 200:
        new_address_id = response1.json()["AddressID"]
        url_upadate_customer = f'http://127.0.0.1:5000/add_customer_address?customer_id={customer_id}'
        data_address_id = {
            "AddressID": f"{new_address_id}"
        }
        response2 = requests.post(url_upadate_customer, json = data_address_id)

    else:
        print("Error adding address")

#register_address("wojciech_bukala@outlook.com", "Wittiga", "6", "53-514", "Wroclaw", "Poland", "728866324")
#register("piotr", "omiecina", "piotr.omiecina@gmail.com", "piotr123")
#register("Wojciech", "Bukala", "wojciech_bukala@outlook.com", "wojtek123")
#login("wojciech_bukala@outlook.com", "wojtek123")

