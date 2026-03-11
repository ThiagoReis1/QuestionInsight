from numpy import*


vtr1= array(eval(input("SEQUENCIA:")))
vtr2= array(eval(input("SEQUENCIA:")))

i=1
v1=0
v2=100

while(i<size(vtr1)):
	if(vtr1[i]==5 and vtr2[i]==100):
		v1= v1+1
	elif(vtr1[i]==2.5 and vtr2[i]==50):
		v1=v1+1
	
	i=i+1
if(vtr1==vtr2):
	print(i)
	