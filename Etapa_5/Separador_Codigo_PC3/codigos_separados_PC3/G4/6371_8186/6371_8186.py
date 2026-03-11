from numpy import*

num = array(eval(input("Diga: ")))

v = zeros(size(num),dtype = int)


for i in range(size(num)):
	if(num[i] == 0):
		v[i] = 9**2
	
	else:
		v[i] = (num[i] -1)**2
		
print(v)