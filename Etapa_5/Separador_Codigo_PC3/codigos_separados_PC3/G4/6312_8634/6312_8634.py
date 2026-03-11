from numpy import*
compra = input("Compras: ").upper()
b = 0
c = 0
e = 0
i = 0
while i < len(compra):
	if compra[i] == "B":
		b +=1
	if compra[i] == "C":
		c+=1
	if compra[i] == "E":
		e+=1
	i+=1
soma = (b*3.75)+(c*7.9)+(e*9.85)
print(round(soma, 2), b, c, e)