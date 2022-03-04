# (a,b) = ("Othman", "Ahmad")
# [c,d] = [100, 200]
# print(a,b)
# print(c,d)

fiends = {"othman": 31, "othman2": 28, "ahmad": 27, "Mjh": 30}

print(sorted([(v,k) for k,v in fiends.items()], reverse=True))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])