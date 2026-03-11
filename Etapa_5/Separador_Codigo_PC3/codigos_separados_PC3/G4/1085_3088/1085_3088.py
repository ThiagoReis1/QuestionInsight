n1 = float(input("Primeira prova:"))
n2 = float(input("Segunda prova:"))
n3 = float(input("Terceira prova:"))
n4 = float(input("Quarta prova:"))
n5 = float(input("Quinta prova:"))
man = (n1+n2+n3+n4+n5)/5
if man>=6.0:
	msg = "Aprovacao"
else:
	msg = "Reprovacao"
print(round(man,2))
print(msg)
