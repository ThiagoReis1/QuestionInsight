from numpy import*
v=array(eval(input("Notas ")))
i=0
while(i<size(v)):
	if(v[i]>4 and v[i]<5):
		v[i]=4
	elif(v[i]>9 and v[i]<10):
		v[i]=10
	else:
		v[i]=v[i]
	i=i+1
print(v)