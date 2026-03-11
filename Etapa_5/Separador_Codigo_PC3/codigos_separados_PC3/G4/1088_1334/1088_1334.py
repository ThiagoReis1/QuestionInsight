x=float(input("informe a nota um: "))
y=float(input("informe a nota dois: "))
c=float(input("informe a nota tres: "))
v=float(input("informe a nota quatro: "))
b=float(input("informe a nota cinco: "))
n=(x+y+c+v+b)/5
if (n>=7):
	print(round(n, 2))
	print("Aprovacao")
else:
	print(round(n, 2))
	print("Reprovacao")