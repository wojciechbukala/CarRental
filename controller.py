import endpoints
import requests
from datetime import date

# zmienne lokalne z obecnie zalogowanym użytkownikiem
logged_id = 0
logged_email = "None"
staff_logged_email = "None"

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

# zwraca samochody z podanego segmentu
def get_cars_by_segment(segment):
    url_get_cars = f'http://127.0.0.1:5000/cars_by_segment?segment={segment}'
    response = requests.get(url_get_cars)
    return response.json()


# Zwraca dotępne samochody na podstawie podanych parametrów
def get_available_cars(start_date = '2100-12-31', end_date = '2000-01-01', segment = None, car_brand = None, car_model = None):
    url = 'http://127.0.0.1:5000/get_available_cars'

    data = {
        'start_date': start_date,
        'end_date': end_date
    }

    if segment is not None:
        data['segment'] = segment
    if car_brand is not None:
        data['car_brand'] = car_brand
    if car_model is not None:
        data['car_model'] = car_model

    response = requests.get(url, params = data)

    return response.json()

# wypożycznie samochodu
# pierwszy dostępny samochód z bazy o podanej marce i modelu
# zmienia status w "Car" na rented i wpisuje rekord do tabeli "Rental"
def rent_a_car_transaction(start_date, end_date, car_brand, car_model):
    url_get_car = f"http://127.0.0.1:5000/get_car_by_model?brand={car_brand}&model={car_model}"
    response1 = requests.get(url_get_car)
    car_id = response1.json()[0]
    data_rental = {
        "CarID": f"{car_id}",
        "UserID": f"{logged_id}",
        "StartDate": f"{start_date}",
        "EndDate": f"{end_date}"
    }
    
    url_rent_a_car = 'http://127.0.0.1:5000/rent_a_car'
    response = requests.post(url_rent_a_car, json = data_rental)
    print(response.json())

# Zwraca wypożyczenia zalogowane użytkownika
def get_rentals_logged_cutomer():
    url_rentals = f'http://127.0.0.1:5000/rental_by_customer_id?customer_id={logged_id}'
    response = requests.get(url_rentals)
    return response.json()

# Zwraca Imię, Nazwisko i email pracowników
def get_staff():
    url_staff = f'http://127.0.0.1:5000/staff'
    response = requests.get(url_staff)
    print(response.json())
    return response.json()

# functions under can be used only by staff

# logowanie pracownika tylko na podstawie emaila
def login_staff(email):
    url = f"http://127.0.0.1:5000//login_staff?email={email}"
    response = requests.get(url)

    if response.status_code == 200:
        global staff_logged_email
        staff_logged_email = email
        return 0
    else:
        return 1

# zwraca wszystkie wypożyczenia
def get_all_rentals():
    url_all_rentals = f'http://127.0.0.1:5000/rental_all'
    response = requests.get(url_all_rentals)
    return response.json()

# zwraca wszystkich klientów z bazy
def get_all_customers():
    url_get_customers = f'http://127.0.0.1:5000/get_customers'
    response = requests.get(url_get_customers)
    return response.json()

# transakcja zwrotu samochodu
# car_id zwraca get_available_cars, get_all_rental, get_user_rental
def return_a_car_transaction(car_id):
    data_return = {
        "CarID": f"{car_id}",
    }
    
    url_return_a_car = 'http://127.0.0.1:5000/return_a_car'
    response = requests.post(url_return_a_car, json = data_return)
    return response.json()

# new_stauts 'True' or 'False' (do not use (0,1))
# car_id zwraca get_available_cars, get_all_rental, get_user_rental
def flag_insurance(new_status, car_id):
    url_flag_insurance = f'http://127.0.0.1:5000/update_insurance?new_status={new_status}&car_id={car_id}'
    response = requests.post(url_flag_insurance)

def flag_diagnostics(new_status, car_id):
    url_flag_diagnostics = f'http://127.0.0.1:5000/update_diagnostics?new_status={new_status}&car_id={car_id}'
    response = requests.post(url_flag_diagnostics)

def flag_status(new_status, car_id):
    url_flag_status = f'http://127.0.0.1:5000/update_status?new_status={new_status}&car_id={car_id}'
    response = requests.post(url_flag_status)

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
#register_address("wojciech_bukala@outlook.com", "Wittiga", "6", "53-514", "Wroclaw", "Poland", "728866324")
#register("piotr", "omiecina", "piotr.omiecina@gmail.com", "piotr123")
#register("Wojciech", "Bukala", "wojciech_bukala@outlook.com", "wojtek123")
#login("wojciech_bukala@outlook.com", "wojtek123")
#rent_a_car_transaction('2024-05-09', '2024-05-11', 'Toyota', 'Camry')
#get_available_cars(start_date = '2100-12-31', end_date = '2000-01-01', car_model = 'Camry')
#flag_status('available', 6)
#print(return_a_car_transaction(1))
#login_staff("wojciech_bukala@outlook.com")
#print(get_available_cars(start_date = '2024-04-10', end_date = '2024-04-12', car_model = 'Camry'))


#test 1
# login("wojciech_bukala@outlook.com", "wojtek123")
# rent_a_car_transaction('2024-05-09', '2024-05-11', 'Hyundai', 'Tucson')
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', car_model= 'Tucson'))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', car_brand = 'Hyundai', car_model= 'Tucson'))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', car_model= 'Tucson'))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', segment = 'F',car_brand = 'Hyundai', car_model= 'Tucson'))

#test 2
# login("wojciech_bukala@outlook.com", "wojtek123")
# print(return_a_car_transaction(7))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', car_model= 'Tucson'))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', car_brand = 'Hyundai', car_model= 'Tucson'))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', car_model= 'Tucson'))
# print(get_available_cars(start_date = '2024-05-10', end_date = '2024-05-12', segment = 'F',car_brand = 'Hyundai', car_model= 'Tucson'))