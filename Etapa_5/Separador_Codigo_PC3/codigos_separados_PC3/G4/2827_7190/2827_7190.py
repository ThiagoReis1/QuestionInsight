from numpy import*

v= array(eval(input(";")))
i= 0

while(i<size(v)):
	if(4<v[i]<5):
		v[i]=4
	if(9<v[i]<10):
		v[i]=10
	i = i+1
	
print(v)