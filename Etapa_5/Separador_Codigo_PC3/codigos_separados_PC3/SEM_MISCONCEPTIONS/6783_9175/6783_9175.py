
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
							
pais = input("Digite 'B' para Brasil e 'E' para Estados Unidos: ").upper()
							
ano_consulta = 2023
							
idade = ano_consulta - ano_nascimento
						
if pais == 'B' and pais == 'E':
	print("sim")
	print(idade)
							
elif pais == 'E' and idade >=16:
	print("sim")
	print(idade)
else:
	if pais not in ('B', 'E'):
		print("invalido")
		
		else: 
			print("nao")
			anos_faltando = 18 if pais 