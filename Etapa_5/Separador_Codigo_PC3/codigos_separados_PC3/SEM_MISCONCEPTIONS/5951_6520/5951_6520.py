pedido=input("tapioca ou salgado: ")
if pedido == "T" or "S":
	quantidade=float(input("quantidade: "))
	
acai=float(input("quantidade de acai: "))

tapioca=4.50
salgado=5.00
acaii=12.00

if pedido == "T":
	vtotal=tapioca*quantidade + acai*acaii
else:
	vtotal=salgado*quantidade + acai*acaii
print(round(vtotal,2))
	