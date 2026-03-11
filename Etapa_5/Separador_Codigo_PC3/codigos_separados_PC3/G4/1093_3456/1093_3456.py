N = int(input("entrada ?"))

a = int(int(N//1000))
b = int(int(N//10))

a1 = a**2
a2 = b**2

s = a1+a2

if(N == s):
	mensagem = "atende"
else:
	mensagem = "nao atende"
	
print(mensagem)	
print(N)
