from numpy import*

soma= 100
anel= 0
a= array(eval(input()))
i=0

while anel != 0:
	if anel == 1:
		soma= soma * 5
	elif anel ==2 :
		soma= soma * 3 
	elif anel == 3:
		soma= soma
	elif anel == 4:
		soma= soma/2
	
print(round(soma,2))
	
	
	
	
	
	
	
	
	
	
	
	
	