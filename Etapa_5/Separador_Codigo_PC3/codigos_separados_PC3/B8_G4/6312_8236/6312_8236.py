from numpy import*

x = input("digite a letra do produto: ").upper()

b = 0
c = 0
e = 0
cont = 0
b1 = 3.75
c1 = 7.90
e1 = 9.85

while cont < len(x):
	if x[cont] == "B":
		b += 1
	elif x[cont] == "C":
		c += 1
	elif x[cont] == "E":
		e += 1
	cont += 1
vt = (b * b1)+(c * c1)+(e*e1)
print(round(vt, 2),b,c,e)
