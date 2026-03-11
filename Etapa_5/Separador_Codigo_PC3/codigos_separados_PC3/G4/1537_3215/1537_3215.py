from math import *
x = eval(input())
k = int(input())
r=0
kf=0
z=0


while(r<k):
	aux =((x**z)/factorial(z))   
	kf = kf + aux
	z= z+1
	r = r + 1
		
		
		
print(round(kf,9))