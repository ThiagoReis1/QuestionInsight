from numpy import*
v=array(eval(input("vetor: ")))
cont=0
i=0
while(i<size(v)):
	if(v[i]==1):
		cont=cont+10
	elif(v[i]==2):
		cont=cont+5
	elif(v[i]==3):
		cont=cont+10
	elif(v[i]==4):
		cont=cont+5
	elif(v[i]==5):
		cont=cont+10
	elif(v[i]==6):
		cont=cont+5
	i=i+1
	
print(cont)