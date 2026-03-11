n=int(input())

r1=n//10000
r2=n%10000
r3=(r1+r2)**2

if (n==r3):
	mensagem ="atende"
else:
	mensagem = "nao atende"
print(n)
print(mensagem)
