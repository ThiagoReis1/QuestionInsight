n1 = float(input("nota 01:"))
n2 = float(input("nota 02:"))
n3 = float(input("nota 03:"))
n4 = float(input("nota 04:"))

sn = n1+n2+n3+n4
ma = sn / 4

if (ma>=5):
	mensagem = "Aprovacao"
	
else:	
	mensagem = "Reprovacao"

print(round(ma,2))
print(mensagem)

