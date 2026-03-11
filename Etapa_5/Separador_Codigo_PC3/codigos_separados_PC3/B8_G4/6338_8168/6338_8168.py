from numpy import * 

v=array(eval(input("")))
x=int(input(""))
i=0
acu=0
while(i<size(v)):
	if(v[i]==x):
		print(i)
	elif(v[i]>x):
		acu += 1 
	i +=1
print(acu)