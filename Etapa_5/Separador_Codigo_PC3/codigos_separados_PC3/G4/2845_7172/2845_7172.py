from numpy import*
x=array(eval(input("cyr:")))
y=zeros(size(x),dtype=int)
for i in range(size(x)):
	if(x[i]<9):
		y[i]=x[i]+1
	else:
		y[i]=0
print(y)
	