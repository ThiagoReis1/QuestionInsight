anonasc = int(input("Informe seu ano de nascimento: "))
pais = input("Informe o pais em que deseja dirigir: Brasil(B) ou China(C): ").upper()
idade = 2023 - anonasc

if pais == "B":
	if idade > 21:
		temp = idade - 21
		print ("sim")
		print (temp)
	else:
		falta = 21-idade
		print("nao")
		print(falta)
elif pais == "C":
	if idade > 24:
		temp1 = idade -24
		print ("sim")
		print (temp1)
	else:
		falta1 = 24-idade
		print ("nao")
		print (falta1)
else: 
	print("invalido")