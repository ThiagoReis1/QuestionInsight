item = input("digite o item: ")
quantidade_item = int(input("digite a quantidade: "))
quantidade_acai = int(input("digite a quantidade: "))

tapioca = 5.50
salgado = 4.00
acai= 10.00

if("item" == "T"):
	preco = (quantidade_item * tapioca) + (quantidade_acai * acai)
	
else:
	preco = (quantidade_item * salgado) + (quantidade_acai * acai)
	
print(round(preco, 2))