from math import*

x=eval(input("Num Real: "))
k=float(input("Num Inteiro: "))
a=0
i=0
t=0
while(t<k):
	if(t%2==0):
		a=a+1*((x**t)/factorial(i))
	elif(t%2==1):
		a=a-1*((x**t)/factorial(i))
	i=i+2
	t=t+1
print(round(a,6))
	