from numpy import*
a=input("Digite:").split(',')
b=zeros(6, dtype=int)
i=0
while(i<len(a)):
	if(a[i]=="MC"):
		b[0]=b[0]+1
		i=i+1
	elif(a[i]=="C"):
		b[1]=b[1]+1
		i=i+1
	elif(a[i]=="CM"):
		b[2]=b[2]+1
		i=i+1
	elif(a[i]=="EM"):
		b[3]=b[3]+1
		i=i+1
	elif(a[i]=="E"):
		b[4]=b[4]+1
		i=i+1
	else:
		b[5]=b[5]+1
		i=i+1
print(max(b))		
print(b)		