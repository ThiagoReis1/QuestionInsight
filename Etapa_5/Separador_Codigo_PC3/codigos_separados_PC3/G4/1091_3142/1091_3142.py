# entrada do numero quadrado
N = int(input("Digite o numero: "))

n1 = N // 100
n2 = N % 100
m1 = (n1 + n2 )** 2

if (N == m1):
	print(N)
	print("atende")
else:
	print(N)
	print("nao atende")