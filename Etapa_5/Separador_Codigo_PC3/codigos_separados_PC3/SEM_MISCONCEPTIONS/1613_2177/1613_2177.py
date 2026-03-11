from numpy import*
v=array(eval(input()))
v1=array(eval(input()))

i=0
while(i<size(v)):
	if(v[i]=="ALONGAMENTO"):
		v[i]=3
	elif(v[i]=="CORRIDA"):
		v[i]=10.3
	elif(v[i]=="DANCA"):
		v[i]=6.7
	elif(v[i]=="ESCALADA"):
		v[i]=9.7
	elif(v[i]=="HIDROGINASTICA"):
		v[i]=5
	i=i+1
j=0
k=0
while(j<size(v)):
	k=k+(v[0]*v1[0])+(v[1]*v1[1])+(v[-1]*v1[]-1)
	i=i+1			 
print(round(k,2))