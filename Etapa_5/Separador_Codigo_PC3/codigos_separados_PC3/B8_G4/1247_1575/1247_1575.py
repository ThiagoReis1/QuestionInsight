from numpy import*
Ve=array(eval(input("digite o vetor:")))
a= min(Ve)
b= max(Ve)
c= 0.75 * a + 0.25 * b
d = 0.25 * a + 0.75 * b
x1=0
x2=0

for x in Ve:
	if (x>=a) and (x<c):
		x1=x1+1
	elif (x>=d) and (x<b):
		x2=x2+1
		
W=array([x1,x2])
print(W)