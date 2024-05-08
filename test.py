import requests

url_address = 'http://127.0.0.1:5000/add_address'
data_address = {
    "AddressID": 1,
    "Address1": "Nowa",
    "Address2": "10",
    "PostalCode": "00-002",
    "City": "Warszawa",
    "Country": "Polska",
    "PhoneNumber": "+48987654321"
}

url_customer = 'http://127.0.0.1:5000/add_customer'
data_customer = {
    "FirstName": "Wojciech",
    "LastName": "Bukala",
    "Email": "wojciech_bukala@outlook.com",
    "Password": "wojtek123",
    "AddressID": 1,
    "CreateDate": "2024-05-08"
}
#response = requests.post(url_customer, json = data_customer)

#print(response.json())  # Wyświetla odpowiedź JSON od serwera Flask


def get_customer_by_email(email):
    url = f"http://127.0.0.1:5000/customer?email={email}"
    response = requests.get(url)
    customer = response.json()
    return customer

customer = get_customer_by_email("piotr.omiecina@gmail.com")
#customer = get_customer_by_email("oiotr.pmiecina@gmail.com")
print(customer)