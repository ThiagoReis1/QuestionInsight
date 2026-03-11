destino = input()
idade = int(input())
mult = 0
if(idade<0 or idade>150):
	print("Entradas invalidas")
else:
	if(idade<=2):
		mult=0
	elif(idade<=12):
		mult = 0.5
	elif(idade>=65):
		mult = 0.7
	if(destino == "porto velho"):
		passagem = 500
		print("Passagem: R$",round(passagem*mult,2))
	elif(destino== "santarem"):
		passagem = 370
		print("Passagem: R$",round(passagem*mult,2))
	elif(destino== "belem"):
		passagem = 600
		print("Passagem: R$",round(passagem*mult,2))
	elif(destino == "tefe"):
		passagem = 360
		print("Passagem: R$",round(passagem*mult,2))
	elif(destino=="tabatinga"):
		passagem = 550
		print("Passagem: R$",round(passagem*mult,2))
	else:
		print("Entradas invalidas")