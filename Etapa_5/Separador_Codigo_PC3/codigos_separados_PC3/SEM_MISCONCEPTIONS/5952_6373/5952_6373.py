comida= input("digite t para tapioca e s para salgado:")
quantidade= int(input("digite a quantidade de salgado ou tapioca:"))
quantidade_de_acai= int(input("digite a quatidade de acai:"))
preco_tapioca=3.50
preco_salgado=5.00
preco_acai=13.00
if(comida == "T"):
	
	valor_total = (quantidade * preco_tapioca) + (quantidade_de_acai * preco_acai)

else: 
		valor_total = (quantidade * preco_salgado) + (quantidade_de_acai * preco_acai)
		
print(round(valor_total,2))
