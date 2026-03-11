n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
ma = (n1+n2+n3)/3
if(ma >= 6.0):
	mensagem = ("Aprovacao")
else:
	mensagem = ("Reprovacao")

print(round(ma, 2))
print(mensagem)