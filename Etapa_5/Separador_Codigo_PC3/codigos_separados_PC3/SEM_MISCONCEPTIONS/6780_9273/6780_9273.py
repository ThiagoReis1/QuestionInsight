
nasc = int(input(" "))
pais = input("pais:")
idade = 2023 - nasc

if pais.upper() == "B" and idade >= 21:
	print("sim")
	apto = (2023 - nasc) - 21     
	print(apto)   
elif pais.upper() == "B" and idade <21:
	print("nao")
	falta = 21 - idade 
	print(falta)
elif pais.upper() == "C" and idade >= 24:
	print("sim")
	apto = (2023 - nasc) - 24
	print(apto)
elif pais.upper() == "C" and idade < 24:
	print("nao")
	falta = 24 - idade
	print(falta)  
else: 
	print("invalido") 