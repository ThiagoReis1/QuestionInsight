anoNasc = int(input())
pais = input()
pais = pais.upper()
if(pais == 'B' or pais == 'I'):
	idade = 2023 - anoNasc
	if(pais == 'B' and idade > 17):
		print("sim")
		print(idade - 18)
	elif(pais == 'B'):
		print("nao")
		print(18 - idade)
	elif(idade > 16):
		print("sim")
		print(idade - 17)
	else:
		print("nao")
		print(17-idade)
else:
	print("invalido")