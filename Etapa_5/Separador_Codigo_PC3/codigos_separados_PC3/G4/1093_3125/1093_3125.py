N = int(input("entrada: "))

a = int(N/1000)
b = int(N/100)

a1 = a**2
b1= b**2

s = a1**2 + 2 * a * b + b1 ** 2

if(N == s):
	mensagem = "atende"
else:
	mensagem = "nao atende"
	
print(mensagem)
print(N)