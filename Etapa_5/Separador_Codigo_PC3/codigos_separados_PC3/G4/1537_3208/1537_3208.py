from math import*
x=int(input())
k=float(input("Termos da serie:"))
t=1
j=1
if(k>0):
	while(t<k):
		j=j+(x**t)/t
		t=t+1
	print(round(j,9))
	
	
	