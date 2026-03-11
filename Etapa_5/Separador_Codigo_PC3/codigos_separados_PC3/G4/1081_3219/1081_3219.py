from math import *
p1= float(input())
p2= float(input())
p3= float(input())
p4= float(input())

med=(p1+p2+p3+p4)/4
print(round(med, 2))

if(med>=5.0):
	print("Aprovacao")
else:
	print("Reprovacao")