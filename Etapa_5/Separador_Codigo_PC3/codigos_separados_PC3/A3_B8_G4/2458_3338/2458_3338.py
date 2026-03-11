from math import*

p = float(input("sem desconto: "))
c = float(input("codigo: "))

f1 = 0.10 
f2 = 0.08
f3 = 0.00
f4 = 0.02
d = 0.40
v = (p - p * d) + p * (10 / 100)
v1 = (p - p * d) + p * (8 / 100)
v2 = (p - p * d) + p * (0 / 100)
v3 = (p - p * d) + p * (2 / 100)
if(c == 1):
	print(round(v, 2))
elif(c==2):
	print(round(v1, 2))
elif(c ==3):
	print(round(v2, 2))
elif(c==4):
	print(round(v3, 2))