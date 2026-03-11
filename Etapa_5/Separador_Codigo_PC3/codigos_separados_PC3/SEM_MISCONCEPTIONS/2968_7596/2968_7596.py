produto = input("lanche ou salgado: ")
ql = int(input("quantidade de lanches: "))
qr = int(input("quantidade de suco: "))

lanche = 5.00
salgado = 3.50
refrigerante = 4.00

if (produto == "L"):
	pf = (lanche*ql) + (refrigerante*qr)
else:
	pf = (salgado*ql) + (refrigerante*qr)

print(round(pf,2))