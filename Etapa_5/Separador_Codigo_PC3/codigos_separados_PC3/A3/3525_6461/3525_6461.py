from math import *

x = float(input("Numero real: "))
termos = int(input("Quantidade de termos: "))

count_termos = 0
i = 1
while termos % 2 == 0:
	count_termos = count_termos + 1
	