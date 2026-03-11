#ENTRADA DE DADOS
n=int(input("n?"))

#CALCULO INTERNO
n1=n//100
n2=n%100
p= n1**2 + n2**2

#SAIDA DE DADOS
if (p==n):
	print("atende")
else:
	print("nao atende")
print(n)

