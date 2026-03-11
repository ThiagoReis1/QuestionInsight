nf = int(input("numero fornecido:"))
d1 =(nf// 100)
d2 = (nf % 100)
dx = (d1**2)+(d2**2)
if (dx == nf):
	mensagem = ("atende")
else:
	mensagem = ("nao atende")
print(mensagem)
print(nf)