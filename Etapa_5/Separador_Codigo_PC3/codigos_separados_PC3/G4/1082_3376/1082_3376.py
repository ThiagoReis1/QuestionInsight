p1 = float(input("nota 1: "))
p2 = float(input("nota 2: "))
p3 = float(input("nota 3: "))
p4 = float(input("nota 4: "))
p5 = float(input("nota 5: "))
ma = float((p1+p2+p3+p4+p5)/5)
if ma>=5.0:
	print(round(ma,1))
	print("Aprovado")
else:
	print(round(ma,1))
	print("Reprovado")
