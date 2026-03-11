peso= int(input("Peso de acai em gramas:"))
salg= int(input("Quantidade de salgados:"))
pago= float(input("Valor pago:"))


a= (peso*24)/1000
b= (salg*3)

total=(a+b)

if(total==pago):
	print(round(total,2))
	print("Nao")
	
else:
	print(round(total,2))
	print("Sim")
