from math import*

x = float(input("numero:"))
k = int(input("quantidade:"))
cont2 = 0
cont = 1
somak = 0
while(cont2 < k):
	somak = somak + (x / factorial(cont))
	cont = cont + 2
	cont2 = cont2 + 1
print(round(somak, 8))