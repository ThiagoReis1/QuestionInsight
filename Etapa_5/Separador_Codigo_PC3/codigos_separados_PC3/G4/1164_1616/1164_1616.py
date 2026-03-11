from math import *

n = int(input("Digite um numero: "))
i = 0
sin = 1
seq = 0
num = 1

while (i < n):
	i = i + 1
	seq = seq + (i ** 2)/(4.0 + num) * sin
	sin = sin * -1
	num = num + 2
	
print(round(seq, 8))