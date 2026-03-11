from math import *

x = float(input("Digite o valor de x: "))
k = int(input("Digite a quantidade de termos da serie: "))

senh = 0
i = 0
j = 1

while (i < k):
	senh = senh + ((x ** j) / factorial(j))
	j = j + 2
	i = i + 1

print(round(senh, 9))