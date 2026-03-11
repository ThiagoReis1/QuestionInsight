altura_cicero = 1.8
taxa_cicero = 0.01
altura = float(input("Insira o numero: "))
taxa =  float(input("Insira o numero: "))
ano = 0 
				  
while altura < altura_cicero:
	altura_cicero = altura_cicero + taxa_cicero
	altura = altura + taxa
	ano = ano + 1
print(ano)