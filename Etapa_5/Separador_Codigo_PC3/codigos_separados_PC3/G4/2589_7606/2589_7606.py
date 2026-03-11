from numpy import*
v = array(eval(input("digite")))

lim = v[0]
a = 0

for i in range(1, size(v)):
	if v[i] >= lim:
		a = a + 1
		print(i)
print(a)
 

	
	
	
	
	
	

	
	
	
	
	
	
	#if i >= v[0]:
		#a = a + 1
