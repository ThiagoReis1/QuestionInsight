ano= 2023
idade_minima_brasil = 21
idade_minima_estados_unidos = 18
ano_nascimento = int(input("digite o ano do nascimento:"))
pais = input("digite o pais B para brasil E para Estados unidos:").upper()

idade = (ano - ano_nascimento)

if pais == 'B':
	if idade >=21:
		print("sim")
		print (idade - idade_minima)
	else:
		print("nao")
		print(idade_minima - idade)
		
elif  pais == 'E':
	if idade =>18:
		print("sim")
		print(idade - idade_minima)
	else:
		print("nao")
		print(idade_minima - idade)
else:
	print("invalido")
