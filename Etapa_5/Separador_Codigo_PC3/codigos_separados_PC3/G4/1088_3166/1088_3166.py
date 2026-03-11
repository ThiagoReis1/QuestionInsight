from math import*
n1 = float(input("digite nota 1:"))
n2 = float(input("digite nota 2:"))
n3 = float(input("digite nota 3:"))
n4 = float(input("digite nota 4:"))
n5 = float(input("digite nota 5:"))
med = (n1 + n2 + n3 + n4 + n5)/5
if (med >= 7):
	print(round(med, 2))
	print("Aprovacao")
else:
	print(round(med, 2))
	print ("Reprovacao por nota")