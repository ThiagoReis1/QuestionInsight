n=int(input())
a=n//10000
ra=n%10000
b=ra//100
rb=ra%100
calculo=(a**3)+(b**3)+(rb**3)

if(n==calculo):
	mensagem="atende"
else:
	mensagem="nao atende"
	
print(mensagem, n)