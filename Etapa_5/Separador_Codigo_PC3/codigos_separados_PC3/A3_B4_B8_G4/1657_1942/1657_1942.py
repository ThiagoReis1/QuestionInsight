from numpy import*
v=array(input("qual estado:"))
a=0
CA=0
FL=0
PA=0
WI=0
for i in size(v):
	if(i=='AZ'):
		AZ=AZ+1
	elif(i=='CA'):
		CA=CA+1
	elif(i=='FL'):
		FL=FL+1
	elif(i=='PA'):
		PA=PA+1
	elif(i=='WI'):
		PA=PA+1
print(max(v[i]))
print(v[i])