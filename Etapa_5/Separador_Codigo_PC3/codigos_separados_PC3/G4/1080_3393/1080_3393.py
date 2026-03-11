n1 = float(input("nota da prova:"))
n2 = float(input("nota da prova:"))
n3 = float(input("nota da prova:"))
ma = (n1+n2+n3)/3

if(ma>=5,0):
	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(round(ma,2))
print(mensagem)