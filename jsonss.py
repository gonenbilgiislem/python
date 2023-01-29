import json

import jsons

data = '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(data)
print(y["age"])
print(y["name"])
print(y["city"])

customers = {
    "firstName": "John",
    "lastName": "Doe"
}

customerjson = json.dumps(customers)
print(customerjson)
print(customers)