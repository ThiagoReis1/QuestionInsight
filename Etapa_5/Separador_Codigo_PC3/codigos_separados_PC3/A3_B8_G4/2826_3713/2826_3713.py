from numpy import*
n =array(eval(input()))

i=0
l=0
while (i<size(n)):
	if (n[i]>8):
		n[i]= 10
		i = i+1
	elif(n[i]<2):
		n[i]=0
		i = i+1
print(n)