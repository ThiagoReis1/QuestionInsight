j = int(input())
d1 = (j//100)
d2 = j % 100

if(d1**2+d2**2 == j):
	mensagem = "atende"
else:
	mensagem = "nao atende"
	
print(mensagem)
print(j)