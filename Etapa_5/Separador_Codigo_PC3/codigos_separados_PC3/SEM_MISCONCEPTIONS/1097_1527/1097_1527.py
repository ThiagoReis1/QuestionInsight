#Universidade Federal do Amazonas  - Laís Amorim Reis 21602327

valor = int(input("valor: "))
metade1 = valor//1000
metade2 = valor%1000

if(((metade1-metade2)**2) == valor):
	print(valor," atende a propriedade")
else:
	print((metade1-metade2)**2)
