from numpy import*
a=array(eval(input("")))
b=200
soma=0
while(soma>size(a)):
	if(a==1):
		b*4+soma
	elif(a==2):
		b*2+soma
	elif(a==3):
		b+0+soma
	elif(a==4):
		b/2+soma
print(round(soma, 2))