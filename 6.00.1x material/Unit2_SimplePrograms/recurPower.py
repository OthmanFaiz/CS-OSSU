def recurPower(base, exp):
    if exp == 0:
        return float(1)
    elif exp == 1:
        return base
    else:
        return base * recurPower(base,exp - 1)

print(recurPower(6.74, 0))