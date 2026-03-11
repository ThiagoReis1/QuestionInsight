from math import *
cat1 = float(input("Comprimento do cateto 1(em metros):  "))
cat2 = float(input("Comprimento do cateto 2(em metros):  "))
cust_aplic = float(input("Custo da aplicacao por metro quadrado:  "))

area_triang = (cat1 * cat2) / 2
total = area_triang * cust_aplic

print(round(total, 2))