from math import*

nx = float(input("diga jovi bon: "))
nk = int(input("diga meu nobri: "))

calc = 0
cont = 0
d = 0
s = 1

while(cont < nk):
	calc = (nx ** d) / factorial(d) + calc
	d = 2 + d
	cont = cont + 1 
	
print(round(calc, 8))