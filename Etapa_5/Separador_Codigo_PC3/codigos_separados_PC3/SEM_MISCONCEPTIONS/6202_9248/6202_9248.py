altura_bia = 1.69
taxa_bia = 0.01
altura = float(input('altura: '))
taxa = float(input('taxa: '))
ano = 0
while(altura_bia > altura):
	altura_bia = altura_bia + taxa_bia
	altura = altura + taxa
	ano = ano + 1
print(ano)