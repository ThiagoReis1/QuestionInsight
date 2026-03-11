from numpy import*
v = array(eval(input("")))
i= 0
j = 100

while(i < len(v)):
	if(v[i]==1):
		j = v[i] + j*5 
	elif(v[i]==2):
		j = v[i] + j*3 
	elif(v[i]==3):
		j = v[i] + j 
	elif(v[i]==4):
		j = v[i]/2 + j 
	i=i+1
	
print(round(j,2))