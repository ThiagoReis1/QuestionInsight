n1=float(input("nota 1:"))
n2=float(input("nota 2:"))
n3=float(input("nota 3:"))
n4=float(input("nota 4:"))
n5=float(input("nota 5:"))

mx=(n1+n2+n3+n4+n5)/5

if(mx>=5.0):
	mensagem="Aprovado"
	
else:
	mensagem="Reprovado"
	
print(round(mx,1))
print(mensagem)