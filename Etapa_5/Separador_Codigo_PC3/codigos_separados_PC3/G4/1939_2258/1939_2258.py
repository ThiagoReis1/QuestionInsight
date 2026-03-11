nome = input("Digite o nome do aminoácido desejado (ASPARAGINA ou TRIPTOFANO): ")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if (nome=="ASPARAGINA"):
	mensagem = (3*o) + (2*n) + (8*h) + (4*c)
else:
	mensagem = (2*o) + (2*n) + (11*h) + (11*c)
	
print(round(mensagem,2))