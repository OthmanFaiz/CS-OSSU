dic = { "Othman": 31, "Ahmad": 28, "talal": 33 }

# print(list(dic))
# print(dic.keys())
# print(dic.values())
# print(dic.items())

for name, age in dic.items():
    print(name,age)

stuff = dict()
print(stuff.get('candy',-1))