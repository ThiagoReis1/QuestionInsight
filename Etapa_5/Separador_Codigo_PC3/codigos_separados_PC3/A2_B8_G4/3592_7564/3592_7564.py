from numpy import*
dado = array(eval(input("")))
x=100
i=0
while(i<size(dado)):
	if(dado[i]==1):
		x=x
	elif(dado[i]==2):
		x=x*2
	elif(dado[i]==3):
		x=x/3
	elif(dado[i]==4):
		x=x*4
	elif(dado[i]==5):
		x=x/5
	elif(dado[i]==6):
		x=x*6
	i=i+1
print(round(x,2))