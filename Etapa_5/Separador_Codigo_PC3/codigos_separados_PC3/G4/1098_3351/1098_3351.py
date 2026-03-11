#Entrada
m = int(input("Insira o numero: "))
#Propriedade
a = m//1000
b = m%1000
k = (a - b)**4
#saida
if (k == m):
	print(m)
	print("atende")
else:
	print(m)
	print("nao atende")
