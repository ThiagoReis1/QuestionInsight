from numpy import*
x = input("digite D para doces S para salgados e I para integrais: ").upper()
a = 0
i = 0
while i < len(x):
	if x[i] == "D":
		a = a + 2.25
	elif x[i] == "S":
		a = a + 4.00
	elif x[i] == "I":
		a = a + 6.90
	i = i + 1
print(round(a,2))