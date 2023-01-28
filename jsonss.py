import json

data = '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(data)
print(y["age"])
print(y["name"])
print(y["city"])

customers = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 30,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021"
    },
    "phoneNumber": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "fax",
            "number": "646 555-4567"
        }
    ]
}

print(customers["firstName"])
print(customers["lastName"])
print(customers["age"])
print(customers["address"]["streetAddress"])
print(customers["address"]["city"])
print(customers["address"]["state"])
print(customers["address"]["postalCode"])
print(customers["phoneNumber"][0]["type"])
print(customers["phoneNumber"][0]["number"])
print(customers["phoneNumber"][1]["type"])
print(customers["phoneNumber"][1]["number"])

