T =5.50
S =4.00
a =10

comida=input("S/T:")
comida = comida.upper()

quant= int(input("quant:"))
quant_acai= int(input("quant:"))

qacai=quant_acai*a
if comida=="S":
	valor=S*quant+qacai
else:
	valor=T*quant+qacai

print(valor)