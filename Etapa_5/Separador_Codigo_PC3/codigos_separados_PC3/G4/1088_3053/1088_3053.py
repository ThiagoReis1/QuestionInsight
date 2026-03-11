a = float(input("nota 1: "))
b = float(input("nota 2: "))
c = float(input("nota 3: "))
d = float(input("nota 4: "))
e = float(input("nota 5: "))
M = (a+b+c+d+e)/5
if (M<7):
	m = "Reprovacao por nota"
else:
	m = "Aprovacao"
print(round(M,2))
print(m)