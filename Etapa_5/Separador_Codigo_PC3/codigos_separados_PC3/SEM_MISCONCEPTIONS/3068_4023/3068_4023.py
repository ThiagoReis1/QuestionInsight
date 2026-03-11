nome_arma=input("Digite o nome da arma(CIMITARRA/KATANA/SABRE): " )
destreza=int(input("Digite o valor da sua destreza: "))
d1=int(input("Digite o valor do dado1: "))
d2=int(input("Digite o valor do dado2: "))
s=d1+d2
if (0!=d1<=10) and (0!=d2<=10):
	if (nome_arma=="CIMITARRA"):
		print((2*s)+(2*destreza))
	if (nome_arma=="KATANA"):
		print((2*s)+destreza)
	if (nome_arma=="SABRE"):
		print(s+(2*destreza))
else:
	print("Entrada invalida")
	
