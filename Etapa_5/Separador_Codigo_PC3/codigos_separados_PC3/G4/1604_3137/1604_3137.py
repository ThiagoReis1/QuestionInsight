from numpy import*
a = array(eval(input()))
i = 0
b = 0

while(i < size(a)  ):
	if(a[i] == 1):
		b = b + 80
		i = i + 1 
	elif(a[i] == 2):
		b = b + 40
		i = i + 1 
	elif(a[i] == 3):
		b = b + 20
		i = i + 1 
	else:
		b = b + 10
		i = i + 1 
	
print(int(b))