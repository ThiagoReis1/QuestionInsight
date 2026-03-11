N = int(input("N:"))

a = int(int(N//100))
b = int(int(N % 100))

a1 = a ** 2
b1 = b ** 2

s = a1 + b1
(a1 - 2 * a * b + b1)* ( a1 - 2 * a * b + b1)
if(N == s):
	mensagem = "atende"
else:
	mensagem = "nao atende"
print(mensagem)
print(N)
