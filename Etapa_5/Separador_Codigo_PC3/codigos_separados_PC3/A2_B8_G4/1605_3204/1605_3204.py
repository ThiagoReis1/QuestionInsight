from numpy import*
v = array(eval(input()))

i = 200

while(i<size(v)):
	if(v==1):
		i = i*4
	elif(v==2):
		i = i*2
	elif(v==3):
		i = i
	elif(v==4):
		i =(i/2)
	print(round(i,2))
		