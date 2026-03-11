from numpy import*

x= input("Insira as nacionalidades: ").split(',')

y= zeros(5, dtype=int)

for i in x:
	if(i=='AR'):
		y[0]=y[0]+1
	elif(i=='BR'):
		y[1]=y[1]+1
	elif(i=='CL'):
		y[2]=y[2]+1
	elif(i=='CO'):
		y[3]=y[3]+1
	elif(i=='UY'):
		y[4]=y[4]+1

maior= max(y)
print(maior)
print(y)
	
	






