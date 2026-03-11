from math import *

x = float(input("numero real x: "))
k = int(input("numero inteiro k: "))

car = 0
cont = 1
con1 = 0

while (con1 < k):
	car = car + (x ** cont) / (cont)
	cont = cont + 2
	con1 = con1 + 1
print(round(car, 7))	

