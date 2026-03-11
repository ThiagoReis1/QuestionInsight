from math import*
A=float(input())
B=int(input())
i=3
C=((A**i)/(i))+((A**(i+2))/(i+2))
D=A-C
while(B>0):
	i=i+2
	D=D-(C)
	B=B-1
print(round(D,6))	
	