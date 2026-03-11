altura_macaco = 1.86
taxa_macaco = 0.01
alCo = float(input())
taCo = float(input())
ano = 0 
while(alCo < altura_macaco):
	altura_macaco += taxa_macaco
	ano += 1 
	alCo += taCo
print(ano)