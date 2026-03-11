from math import *
x = float(input("x: "))
k = int(input("quantidade de termos da serie: "))

s = 0
cont = 1
i = 0

while k > i:
	s = s + x/factorial(cont)
	cont = cont + 2
	i = i + 1
print(round(s, 8))
	