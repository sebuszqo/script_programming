import json

# file to test different things
file = open('data.json')

data = json.load(file)


# for i in data["cars"]:
#     if i["brand"] == "bmw" and i["number"] > 0:
#         i["number"] -= 1
#         print(i["number"])

mydata = ["sebastianek", "bmw"]

data['clients'].append({
                        "name": mydata[0],
                        "car": mydata[1],
                        "transaction": "sell",
                        "sum": 22
                    })
print(data['clients'])
# print(data['cars'])


print("seba".capitalize())




# for i in data['clients']:
#     if i["name"] == "Sebastian":
#         print(i["car"])