from numpy import*

v1 = array(eval(input()))

i=0
j=100
while():
	if(v1.any()==1):
		j=j*1
	elif(v1.any()==2):
		j=j*2
	elif(v1.any()==3):
		j= j*(1/3)
	elif(v1.any()==4):
		j=j*4
	elif(v1.any()==5):
		j=j*(1/5)
	elif(v1.any()==6):
		j=j*6
	i+=1
print(round(j))