from numpy import*
x = array(eval(input("")))
a=0
j = 0
for i in range(size(x)):
	if(x[i]>=70):
		a=a+1
	b = zeros(a,dtype=int)
	
for i in range(size(x)):
	if(x[i]>=70):
		b[j]=i
		j=j+1
		
print(a)
print(b)