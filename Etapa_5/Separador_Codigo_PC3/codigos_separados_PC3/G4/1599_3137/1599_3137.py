from numpy import*
p = array(eval(input("p:")))
a=0
t=0
while( a != size(p)):
	if(p[a]>80):
		t =t + (p[a]-(p[a]*0.15))
		a = a + 1
	else:
		t=t+p[a]
		a=a+1

print(round(t, 2))