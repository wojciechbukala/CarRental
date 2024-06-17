import endpoints
import requests
from datetime import date

# zmienne lokalne z obecnie zalogowanym użytkownikiem
logged_id = 0
logged_email = "None"

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
        global logged_email
        logged_email = email
        global logged_id
        logged_id = response.json()[0][0]
        return 0
    else:
        return 1

def register_new_car():
    url_car = 'http://127.0.0.1:5000/add_car'

def register_address(email, address1, address2, postal_code, city, country, phone_number):
    
    customer_id = get_customer_by_email(email)[1][0][0]
    
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

# functions under can be used only after logging in

def get_available_cars(start_date = '2100-12-31', end_date = '2000-01-01'):
    url_get_available_cars = f'http://127.0.0.1:5000/get_available_cars?start_date={start_date}&end_date={end_date}'
    response = requests.get(url_get_available_cars)
    return response.json()

def get_cars_by_segment(segment):
    url_get_cars = f'http://127.0.0.1:5000/cars_by_segment?segment={segment}'
    response = requests.get(url_get_cars)
    return response.json()

def get_available_cars_by_segment(segment, start_date = '2100-12-31', end_date = '2000-01-01'):
    url_get_available_cars_by_segment = f'http://127.0.0.1:5000/get_available_cars_by_segment?start_date={start_date}&end_date={end_date}&segment={segment}'
    response = requests.get(url_get_available_cars_by_segment)
    return response.json()

def rent_a_car(rental_start, rental_end, car_brand, car_model):
    url_get_car = f"http://127.0.0.1:5000/get_car_by_model?brand={car_brand}&model={car_model}"
    response1 = requests.get(url_get_car)
    car_id = response1.json()[0]
    data_rental = {
        "RentalDate": f"{rental_start}",
        "ReturnDate": f"{rental_end}",
        "CarID": f"{car_id}",
        "CustomerID": f"{logged_id}"
    }

    url_rent_a_car = 'http://127.0.0.1:5000/add_new_rental'
    response2 = requests.post(url_rent_a_car, json = data_rental)


def rent_a_car_transaction(car_id, user_id, start_date, end_date):
    data_rental = {
        "CarID": f"{car_id}",
        "UserID": f"{user_id}",
        "StartDate": f"{start_date}",
        "EndDate": f"{end_date}"
    }
    
    url_rent_a_car = 'http://127.0.0.1:5000/rent_a_car'
    response = requests.post(url_rent_a_car, json = data_rental)
    print(response.json())


def get_rentals_logged_cutomer():
    url_rentals = f'http://127.0.0.1:5000/rental_by_customer_id?customer_id={logged_id}'
    response = requests.get(url_rentals)
    return response.json()

# functions under can be used only by staff

def get_all_rentals():
    url_all_rentals = f'http://127.0.0.1:5000/rental_all'
    response = requests.get(url_all_rentals)
    return response.json()

# new_stauts 'True' or 'False' (do not use (0,1))
def flag_insurance(new_status, car_id):
    url_flag_insurance = f'http://127.0.0.1:5000/update_insurance?new_status={new_status}&car_id={car_id}'
    response = requests.post(url_flag_insurance)

def flag_diagnostics(new_status, car_id):
    url_flag_diagnostics = f'http://127.0.0.1:5000/update_diagnostics?new_status={new_status}&car_id={car_id}'
    response = requests.post(url_flag_diagnostics)

#get_available_cars_by_segment("'B'")
#get_cars_by_segment("'B'")
#get_available_cars()
#login("jan.kowalski@gmail.com", "jan123")
# available_cars = get_available_cars()
# for car in available_cars:
#     print(car)
#flag_insurance('False', 3)
#flag_diagnostics('False', 3)
#rent_a_car('2024-05-09', '2024-05-11', 'Toyota', 'Camry')
#rent_a_car('2024-05-12', '2024-05-14', 'Toyota', 'Camry')
#get_rentals_logged_cutomer()
#get_all_rentals()
#print(logged_email)
#print(logged_id)
#register_address("wojciech_bukala@outlook.com", "Wittiga", "6", "53-514", "Wroclaw", "Poland", "728866324")
#register("piotr", "omiecina", "piotr.omiecina@gmail.com", "piotr123")
#register("Wojciech", "Bukala", "wojciech_bukala@outlook.com", "wojtek123")
#login("wojciech_bukala@outlook.com", "wojtek123")
rent_a_car_transaction(1, 1, '2024-05-09', '2024-05-11',)

