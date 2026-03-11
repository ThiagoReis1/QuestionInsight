n = int(input("Digite o numero: "))
dm = n//100
rn = n%100


condicao = (dm + rn)**2 == n
if condicao :
	print(n, "atende")
else:
	print(n, "nao atende")
