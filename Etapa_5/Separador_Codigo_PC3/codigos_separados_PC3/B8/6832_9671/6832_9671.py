from numpy import *

secao = input("insira 'H' para hortifruti, 'C' para cereais ou 'L' para laticinios: ").upper()

hortifruti = 5.40
cereal = 8.95
laticinios = 4.50

i = 0
h = 0
c = 0
l = 0

while i < len(secao):
	if secao[i] == 'H':
		h = h + 1
	elif secao[i] == 'C':
		c = c + 1
	elif secao[i] == 'L':
		l = l + 1
	i = i + 1
	total = (h * hortifruti) + (c * cereal) + (l * laticinios)
	
print(round(total, 2))