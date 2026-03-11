from math import *

quantos_kwh = (float(input("abrir kwh consumido no mes: ")))


total = quantos_kwh * 0.43 + 10
total_final =  total + total(25/100)


print(round(total_final, 2))