import requests

url = 'http://127.0.0.1:5000/add_address'
data = {
    "AddressID": 2,
    "Address1": "Nowa",
    "Address2": "10",
    "PostalCode": "00-002",
    "City": "Warszawa",
    "Country": "Polska",
    "PhoneNumber": "+48987654321"
}
response = requests.post(url, json = data)

print(response.json())  # Wyświetla odpowiedź JSON od serwera Flask