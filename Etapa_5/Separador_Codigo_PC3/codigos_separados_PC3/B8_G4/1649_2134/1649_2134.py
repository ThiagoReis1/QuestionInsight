from numpy import*

x=input("digite:").split(',')


a=zeros(5, dtype=int)

for i in x:
	if(i=="P"):
		a[0]=a[0]+1
	if(i=="C"):
		a[1]=a[1]+1
	elif(i=="M"):
		a[2]=a[2]+1
	elif(i=="V"):
		a[3]=a[3]+1
	elif(i=="A"):
		a[4]=a[4]+1
	
print(max(a))
print(a)



	

