from distutils.log import info
import json

data = '''[
    {
        "id": "001",
        "x": "2",
        "name": "Othman"
    },{
        "id": "009",
        "x": "7",
        "name": "Ahmad"
    }
]'''

info = json.loads(data)
print("User Count", len(info))

for item in info:
    print("Name:", item["name"])
    print("Id:",item["id"])
    print("Attr:", item["x"])