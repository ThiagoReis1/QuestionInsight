altura_chico = 1.5
taxa_chico = 0.02

altura_pessoa = float(input())
taxa_pessoa = float(input())
tempo = 0

while(altura_pessoa < altura_chico):
	altura_chico += taxa_chico
	altura_pessoa += taxa_pessoa
	tempo += 1
	
print(tempo)