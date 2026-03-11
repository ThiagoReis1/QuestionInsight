n1=float(input("valor:"))
n2=float(input("valor:"))
n3=float(input("valor:"))
n4=float(input("valor:"))
n5=float(input("valor:"))
med=(n1+n2+n3+n4+n5)/5
print(round(med,2))
if (med>=7.0):
	mensagem="Aprovacao"
else:
	mensagem="Reprovacao por nota"
print(mensagem)