nf = int(input(""))

a = nf // 10000
b = (nf % 10000) // 100
c = (nf % 10000) % 100


r = (a**3)+(b**3)+(c**3)

if (nf == r):
	mensagem = "atende"
	
else:
	mensagem = "nao atende"
	
print(mensagem)