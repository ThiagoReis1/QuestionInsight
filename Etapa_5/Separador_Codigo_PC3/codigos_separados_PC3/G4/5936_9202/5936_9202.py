kwh = float(input("kwh"))
t1 = (kwh*0.43) + 10
icms = t1*0.25
total = t1+icms
print(round(total,2))