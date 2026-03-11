from math import*
A=float(input("Peso da Encomenda:"))
B=A*0.05
if(A <= 5000):
		print(round(B,2))
else:
		D=A*0.04+60
		print(round(D,2))