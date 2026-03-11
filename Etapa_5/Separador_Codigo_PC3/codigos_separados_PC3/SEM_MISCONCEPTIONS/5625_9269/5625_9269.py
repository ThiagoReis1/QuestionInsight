item = input("digite o nome: ")
quant = int(input("digite a quantiddade: "))
quant_acai = int(input("digite a quantidade de acai: "))

tapioca = 5.50
salgado = 4.00
acai = 10.00

if (item == "T"):
	valor = (quant*tapioca) + (quant_acai*acai)
	
else:
	valor = (quant*salgado) + (quant_acai*acai)

print(valor)