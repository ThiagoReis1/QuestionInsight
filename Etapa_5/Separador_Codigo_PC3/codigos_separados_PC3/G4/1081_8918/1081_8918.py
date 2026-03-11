from numpy import*
n1 = float(input("nota: "))
n2 = float(input("nota: "))
n3 = float(input("nota: "))
n4 = float(input("nota: "))

c = (n1 + n2 + n3 + n4)/4
print(round(c,2))
if c >= 5:
	print("Aprovacao")
else:
	print("Reprovacao")
