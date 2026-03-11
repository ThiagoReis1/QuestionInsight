from numpy import *
vm = array(eval(input("")))
va = array(eval(input("")))
i = 0
t = 0
a = 0
l = 0
while(i < size(va)):
	a = (va[i]*5)/100
	l = vm[i]*a + l
	i=i+1
	t=t+1
print(l)
		
