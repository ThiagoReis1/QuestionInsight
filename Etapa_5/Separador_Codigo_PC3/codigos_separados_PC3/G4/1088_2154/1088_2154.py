a = float(input("nota: "))
b = float(input("nota: "))
c = float(input("nota: "))
d = float(input("nota: "))
e = float(input("nota: "))

nota = (a+b+c+d+e)/5
n = round(nota, 2)
if(n >= 7.0):
	print(n)
	print("Aprovacao")
else:
	print(n)
	print("Reprovacao por nota")