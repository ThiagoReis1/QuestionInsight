from numpy import*

a = array(eval(input()))

i = 0
p = 0

while(i < size(a) and i != 4):
	if(a[i] == 1):
		p = p + 80
	elif(a[i] == 2):
		p = p + 40
	elif(a[i] == 3):
		p = p + 20
	
	i = i + 1

print(int(p))