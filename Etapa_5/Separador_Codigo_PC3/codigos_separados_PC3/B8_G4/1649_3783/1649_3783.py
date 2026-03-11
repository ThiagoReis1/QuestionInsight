from numpy import*
v= (input('cor dos olhos:'))
y= v.split(',')
x= zeros(5,dtype=int)
for i in y:
	if i== 'P':
	   x[0]+=1
	elif i=='C':
	    x[1]+=1
	elif i== 'M':
	    x[2]+=1
	elif i== 'V':
	   x[3]+=1
	elif i== 'A':
	   x[4]+=1
print(max(x))
print(x)
	
	
		
