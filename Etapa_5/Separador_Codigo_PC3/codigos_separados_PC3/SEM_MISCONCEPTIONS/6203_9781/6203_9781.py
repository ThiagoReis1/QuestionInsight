altura_macaco = 1.4
taxa_macaco = 0.06
AL = float(input("insira a altura"))
TL = float(input("insira a taxa"))

ano = 0

while(altura_macaco < AL):
	altura_macaco = altura_macaco + taxa_macaco
	AL = AL + TL
	ano = ano + 1
print(ano)
	