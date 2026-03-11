from math import*

kWh= float(input("Quantos Kwh consumiu?: "))
total = 10 + (0.43*kWh)
total2 = total*0.25
soma = total + total2
print(round(soma, 2))