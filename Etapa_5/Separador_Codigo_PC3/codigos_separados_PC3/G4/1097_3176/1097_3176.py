nf = int(input("numero:"))

a = nf//1000
b = nf % 1000

f = (a-b)**2

if (nf ==  f):
	mensagem = "atende"
	
else:
	mensagem = "nao atende"
	

print(mensagem)
print(nf)





