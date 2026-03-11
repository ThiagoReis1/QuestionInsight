p1 = float(input("nota 1: "))
p2 = float(input("nota 2: "))
p3 = float(input("nota 3: "))
p4 = float(input("nota 4: "))
ma = (p1+p2+p3+p4)/4
print(round(ma,1))
if (ma>=6.0):
	mensagem="Aprovado"
	
else:
	mensagem="Reprovado"
print(mensagem)
	
		