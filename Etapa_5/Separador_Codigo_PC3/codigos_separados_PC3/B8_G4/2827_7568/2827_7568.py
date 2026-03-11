from numpy import*

n = array(eval(input(' ')))
i = 0
while(i<size(n)):
	if(4<n[i]<5):
		n[i] = 4.0
	elif(9<n[i]<10):
		n[i] = 10.0
	i = i+1

print(n)
	
	
		
		
