mi = int(input())
anos = int(input())

cont = 0

while (anos > cont):
	mi = mi - (mi * 5/100)
	cont = cont + 1
	print(round(mi, 2))