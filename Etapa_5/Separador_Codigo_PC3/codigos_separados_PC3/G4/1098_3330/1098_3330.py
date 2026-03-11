nf = int(float(input("numero fornecido: ")))
d1 = (nf//1000)
d2 = (nf%1000)
if ((d1 - d2)**4)==nf:
	mensagem = ("atende")
else:
	mensagem = ("nao atende")
	
print(nf)
print(mensagem)
