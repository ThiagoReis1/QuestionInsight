n = int(input("informe um numero de tres digitos: "))

n1 = n // 100
n2 = (n//10) % 10
n3 = n % 10

condicao = (n1**3) + (n2**3) + (n3**3)

if(n == condicao):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")