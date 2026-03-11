altura_luna = 1.65
taxa_luna = 0.02
altura = float(input("altura: "))
taxa = float(input("taxa: "))
cresA = altura_luna + taxa_luna
cresB = altura + taxa
ano = 0
while altura < altura_luna:
	ano = ano + 1
	altura = altura + taxa
	altura_luna = altura_luna + taxa_luna
	
print(ano)
	