from numpy import*
x=array(eval(input("x:")))
i=0
while(i!=size(x)):
	if(x[i]>=4 and x[i]<=5):
		x[i]=4
		i=i+1
	elif(x[i]>=9 and x[i]<=10):
		x[i]=10
		i=i+1
	else:
		i=i+1
print(x)