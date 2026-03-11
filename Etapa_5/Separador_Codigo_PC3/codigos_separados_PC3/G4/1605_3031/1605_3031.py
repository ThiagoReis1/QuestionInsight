from numpy import*


v = array(eval(input("")))

i = 0
p = 0

while(v[i]<4):
	
	if(v[i]==1):
		p = p + 4*200
	elif(v[i]==2):
		p = p + 2*200
	elif(v[i]==3):
		p = p + 200
	else:
		p = p + 200/2
	i = i + 1
print(round(p,2))
		
		
	