kwh = float(input("kwh:"))
consumo=  kwh * 0.43
serv = consumo + 10.0
total = serv + (0.25 * serv)
print(round(total, 2))