from numpy import *
a = float(input("nota 1 "))
b = float(input("nota 2 "))
c = float(input("nota 3 "))
d = float(input("nota 4 "))
f =  (a+b+c+d)/4
if  f>= 6.0:
	print(round(f,1))
	print("Aprovado")
else:
	print(round(f,1))
	print("Reprovado")