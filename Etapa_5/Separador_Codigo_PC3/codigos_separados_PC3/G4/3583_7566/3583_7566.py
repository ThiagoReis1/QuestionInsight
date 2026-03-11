from numpy import *
a = array(eval(input("insira os precos: ")))
i = 0
s = 0
while(i<size(a)):
	if(a[i]>50):
		s = s  + a[i] - a[i]*0.08
	else:
		s = s + a[i]
	i +=1
print(round(s, 2))