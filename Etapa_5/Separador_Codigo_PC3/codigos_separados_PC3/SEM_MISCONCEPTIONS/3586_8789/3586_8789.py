from numpy import*

num= array(eval(input()))

i=0
cont=1
while i < size(num):
	if num[i]==1:
		cont=cont*100
	elif num[i]==2:
		cont=cont*60
   elif num[i]==3:
		cont=cont*20
	elif num[i]==4:
	   cont=cont
	i=i+1
	
print(cont)