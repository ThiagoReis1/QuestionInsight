altura_chico = 1.5
taxa_chico = 0.02
altura = float(input("Altura de uma pessoa: "))
taxa = float(input("Taxa de crescimento: "))
ano = 0 

while altura < altura_chico:
	altura = altura + taxa
	
	altura_chico = altura_chico + taxa_chico
	
	ano = ano + 1
	
print(ano)