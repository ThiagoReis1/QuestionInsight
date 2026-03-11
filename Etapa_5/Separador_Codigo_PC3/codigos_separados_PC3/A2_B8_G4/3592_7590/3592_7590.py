from numpy import*

v = array(eval(input("")))

i = 0
j = 100

while(i<size(v)):
	if(v[i]==1):
		j = j 
	elif(v[i]==2):
		j = 2*j
	elif(v[i]==3):
		j = j/3
	elif(v[i]==4):
		j = 4*j
	elif(v[i]==5):
		j = j/5
	elif(v[i]==6):
		j = 6*j
	i = i + 1
	
print(round(j,2))