from numpy import*
v = array(eval(input()))
i = 0
b = 200
while(i < size(v)):
	if(v[i] == 1):
		b = b * 4
		i = i + 1
	elif(v[i] == 2):
		b = b * 2
		i = i + 1
	elif(v[i] == 3):
		b = b
		i = i + 1
	elif(v[i] == 4):
		b = b/2
		i = i + 1
print(round(b,2))		 				