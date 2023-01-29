import json

with open('users.json') as users:
    data = json.load(users)
    # print(data)
    # for user in data:
    #     print("Adı : " + user['name'])
    #     print("Soyadı : " + user['email'])
    #     print(user['address']['street'])
    #     print(f'Aparman adı : {user["address"]["suite"]}, Şehri : {user["address"]["city"]}')
    #     print("---------------------------------")
    # print(data[0]['name'])
    # print(data[0]['email'])
    # print(data[0]['address']['street'])

for x in range(len(data)):
    print(data[x]['name'])
    print(data[x]['email'])
    print(data[x]['address']['street'])
    print("---------------------------------")

    