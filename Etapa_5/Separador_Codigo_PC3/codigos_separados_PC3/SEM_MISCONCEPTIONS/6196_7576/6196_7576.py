altura_chico = 1.5
taxa_chico = 0.02

alt = float(input("altura: "))
taxa = float(input("taxa: "))

ano = 0

while(altura_chico>alt):
	alt = alt + taxa
	altura_chico = altura_chico + taxa_chico
	ano = ano + 1
	
print(ano)	
