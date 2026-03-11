from numpy import*
v=array(eval(input()))
b=array(eval(input()))
i=0
d=0
while(i<size(v)):
	if(v[i]=='CENOURA'):
		d=d+2*b[i]
	elif(v[i]=='FERRO'):
		d=d+4*b[i]
	elif(v[i]=='DWARVEN'):
		d=d+8*b[i]
	elif(v[i]=='ELVEN'):
		d=d+11*b[i]
	elif(v[i]=='DAEDRIC'):
		d=d+14*b[i]
	i=i+1
print(d)
	








