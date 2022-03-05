import json
data = '''{
    "name": "Othman",
    "phone": {
        "type": "intl",
        "number": "+965 900 90 999"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)

print("Name", info["name"])
print("Hide", info["email"]["hide"])