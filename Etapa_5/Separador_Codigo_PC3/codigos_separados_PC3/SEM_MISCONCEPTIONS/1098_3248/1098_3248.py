N = float(input("digite um numero: "))             #numero com 6 digitos

pp = N // 1000
sp = pp % 1000

if((pp - sp)** 4 == N):
	mensagem = "atende"
	
else:
	mensagem = "nao atende"
	
print()
	print(mensagem)
