#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549

N = int(input("Insira a quantidade de termos:"))
y = 3
i = 1
x = 1
e = 0
S = (1 ** 2)/(1 + 3)
while (N >= i):
	if (i % 2 == 0):
		S = S - e
	else:
		S = S + e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 2) / (1 + y)
print(round(S, 7))