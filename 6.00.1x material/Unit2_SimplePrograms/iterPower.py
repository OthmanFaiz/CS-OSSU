def iterPower(base, exp):
    result = 1
    for n in range(exp):
        result *= base
    return result

print(iterPower(5,2))