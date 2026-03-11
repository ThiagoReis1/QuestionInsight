from numpy import*

produto = input("Produtos: ").upper()

i = 0
q = 0

while i < len(produto):
	if produto[i] == "M":
		q = q + 7.25
	if produto[i] == "P":
		q = q + 4.75
	if produto[i] == "R":
		q = q + 3.50
	i = i + 1
print(round(q , 2))

