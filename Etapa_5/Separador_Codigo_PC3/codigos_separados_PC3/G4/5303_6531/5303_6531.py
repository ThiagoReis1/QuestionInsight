x = int(input("digite o valor: "))

qi = x
taxa = 10/100
ano = 0

while( qi >= 0.5):
	rend = qi * taxa
	qi = qi - rend
	ano = ano + 1
print(ano)

	
	
	