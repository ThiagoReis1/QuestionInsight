from numpy import*

v=array(eval(input("entradas notas: ")))

i =0
j = 10

while(i< size(v)):
	if(v[i]>8.0):
		v[i]=10.0
		
	elif(v[i]<2.0):
		v[i]=0
	i = i +1		
print(v)