from numpy import*
v=array(eval(input("")))
i=0
j=0
while(i<size(v)):
	if(v[i]==1):
		j=j+100
	elif(v[i]==2):
		j=j+60
	elif(v[i]==3):
		j=j+20
	elif(v[i]==4):
		j=j
	i=i+1
print(j)