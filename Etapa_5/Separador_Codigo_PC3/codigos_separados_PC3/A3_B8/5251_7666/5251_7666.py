fate = input()
age = int(input())
valor = 0

if(fate == "porto velho"):
	valor = 500
elif(fate == "santarem"):
	valor = 370
elif(fate == "belem"):
	valor = 600
elif(fate == "tefe"):
	valor = 360
elif(fate == "tabatinga"):
	valor = 550

if(valor == 0)or(age < 0)or(age > 150):
	print("Entradas invalidas")
else:
	if(age <= 2):
		valor = 0
	if(age > 2)and(age < 13):
		valor = valor/2
	if(age > 65):
		valor = valor*0.7
	
	print("Passagem: R$",round(valor,2))