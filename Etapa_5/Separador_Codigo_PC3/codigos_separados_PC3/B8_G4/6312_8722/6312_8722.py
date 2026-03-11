from numpy import*

produto = input("Digite o produto: ").upper()
i = 0
acm = 0
b = 0
c = 0
e = 0

while i < len(produto):
	if produto[i] == "B":
		acm = acm + 3.75
		b += 1
	elif produto[i] == "C":
		acm = acm + 7.9
		c += 1
	elif produto[i] == "E":
		acm = acm + 9.85
		e += 1
	i += 1

print(round(acm,2), b, c, e)
	