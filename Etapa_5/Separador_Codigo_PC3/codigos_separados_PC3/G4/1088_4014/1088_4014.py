p1=float(input("primeira prova: "))
p2=float(input("segunda prova: "))
p3=float(input("terceira prova: "))
p4=float(input("quarta prova: "))
p5=float(input("quinta prova: "))
m=(p1 + p2 + p3 + p4 + p5)/5
print(round(m, 2))
if(m>=7.0):
	print("Aprovacao")
else:
	print("Reprovacao por nota")
	