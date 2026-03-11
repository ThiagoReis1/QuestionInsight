n=float(input())
n1= n // 1000
resto_n1=n%1000
resultado=(n1+resto-n1)**4
print(resultado)
if resultado == 81:
	print("nao atende")
else:
	print("atende")
