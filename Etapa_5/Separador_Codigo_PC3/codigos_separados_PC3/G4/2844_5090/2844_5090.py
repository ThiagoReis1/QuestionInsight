from numpy import*

v = array(eval(input("codigo secreto: ")))


for i in range(size(v)):
	if(v[i]==0):
		v[i]= 9
	else:
		v[i]= v[i]-1
	
print(v)