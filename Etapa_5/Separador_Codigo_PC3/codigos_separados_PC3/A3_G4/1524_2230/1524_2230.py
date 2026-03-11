from numpy import *

qi = int(input("Quantidade incial de grifos: "))

x = int(input("Quantidade de novos grifos: "))

y = int(input("Grifos contaminados: "))

i = 0

while(qi < 0):
	p = (qi + x) - y
	i = i + 1
print(i)