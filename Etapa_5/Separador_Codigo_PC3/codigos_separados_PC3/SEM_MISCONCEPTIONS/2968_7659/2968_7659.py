var1 = input("digite (L/S): ")
quantidade = int(input("digite a quantidade:"))
qrefrigerante = int(input("digite a quantidade:"))

lanche = 5.00
salgado = 3.50
refrigerante = 4.00

preco1 = (lanche*quantidade) + qrefrigerante*refrigerante
preco2 = (salgado*quantidade) + qrefrigerante*refrigerante

if(var1.upper()=="L"):
	msg = preco1
else:
	msg = preco2

print(round(msg, 2))