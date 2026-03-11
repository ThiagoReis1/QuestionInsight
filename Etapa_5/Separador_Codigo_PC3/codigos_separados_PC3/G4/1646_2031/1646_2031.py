from numpy import*

vt = array(eval(input("")))

np=0

for i in range(size(vt)):
	if(vt[i] <= 50):
		np=np+1
print (np)
print ()
