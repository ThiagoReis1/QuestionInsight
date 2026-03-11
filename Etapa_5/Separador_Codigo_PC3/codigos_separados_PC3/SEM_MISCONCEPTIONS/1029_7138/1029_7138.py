cons = float(input("consumo de chamadas: "))

cons = cons * 0.28

total = cons + 23

pagar = total + (total*31/100)

print(round(pagar, 2))