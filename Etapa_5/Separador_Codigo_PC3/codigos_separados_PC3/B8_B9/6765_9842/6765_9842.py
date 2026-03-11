idade = int(input("informe ano de nascimento: "))
pais = str(input("B ou R: "))

if(pais.upper() == 'B'):
	total = (2023 - idade)

	if(total >= 18):
		print("sim")
		print(total - 18)
	else:
		if(total < 18):
			print("nao")
			print(18 - total)
else:
	print("invalido")

	if(pais.upper() == 'R'):
		total = (2023 - idade)

		if(total >= 21):
			print("sim")
			print(total - 21)
		else:
			if(total < 21):
				print("nao")
				print(total)
			else:
				print("invalido")
					
			

