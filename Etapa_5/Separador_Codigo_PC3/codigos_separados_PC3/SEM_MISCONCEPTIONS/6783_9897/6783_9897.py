data = int(input('insira a data de nascimento: '))
pais = input('(B) brasil ou (E) estados unidos: ').upper()
idade = 2023 - data 

if pais == 'B':
	if idade >= 18:
		print('sim')
		print(idade - 18)
	else:
		print('nao')
		print(18 - idade)
elif pais == 'E':
	  if idade >= 16:
	   print('sim')
	   print(idade - 16)
	else:
		print('nao')
		print(18 - idade)
else:
	 print('invalido')

	

	 
