altura_chico = 1.5
taxa_chico = 0.02

altura_alunoz = float(input(''))
taxa_alunoz = float(input(''))

ano = 0

while(altura_alunoz < altura_chico):
	altura_chico = altura_chico + taxa_chico
	altura_alunoz = altura_alunoz + taxa_alunoz
	
	ano += 1
	
print(ano)


