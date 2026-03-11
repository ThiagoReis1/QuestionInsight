from math import *

x = float(input("insira um numero real: "))
k = int(input("quantidade de termos: "))

t = 0
s = 0

while t < k:
	s = s + (x ** (t*2))/factorial(t*2)
	t += 1
print(round(s, 8))