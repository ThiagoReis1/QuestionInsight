from numpy import*

v = array(eval(input("osc: ")))

cont = 0

for i in range(1,size(v)):
	if(v[i] >= v[0]):
		print(i)
		cont = cont + 1
	
		
print(cont)		
	
	