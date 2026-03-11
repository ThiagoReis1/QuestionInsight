p1 = float(input("Prova um: "))
p2 = float(input("Prova dois: "))
p3 = float(input("Prova tres: "))
p4 = float(input("Prova quatro: "))
r = (p1 + p2 + p3 + p4)/4
if(r >= 5):
	print(round(r, 2))
	print("Aprovacao")
else:
	print(round(r, 2))
	print("Reprovacao")