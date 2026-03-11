var = float(input("quantidade de kwh consumida?"))
total = (var*0.43)+10
valor = (25*total/100)+total
print(round(valor, 2))