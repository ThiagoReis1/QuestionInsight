from math import*
x=eval(input("Radianos:"))
k=float(input("Termos da serie:"))
t=0	 
sm=0
e=1
while(t<k):
	if(t%2==0):
		j=(x**e)
		s=j/factorial(e)
		sm=1+s
		e=e+2
		t=t+1
		
	else:
		j=(x**e)
		s=j/factorial(e)
		sm=1-s
		e=e+2
		t=t+1
print(round(sm,6))