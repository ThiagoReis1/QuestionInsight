nasc = int(input("Digite o ano do nascimento: "))
pais = input("Digite B para brasil e J para japao: ").upper()

idade = 2023-nasc

dif2 = 20 - idade

if (pais== 'B'):
	if (idade >= 21):
		print("sim")
		print(idade-21)
	else:
		print("nao") 
		print (21-idade)
elif (pais == 'J'):
	if (idade >= 20):
		print("sim")
		print (idade-20)
	else:
		print ("nao")
		print (20-idade)
else:
	print('invalido')