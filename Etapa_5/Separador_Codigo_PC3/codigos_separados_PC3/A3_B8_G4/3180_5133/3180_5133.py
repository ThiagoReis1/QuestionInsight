from numpy import * 

a = array(eval(input()))
tI = 0

n = zeros(4,dtype=int) 
for i in range(size(a)):
	if a[i] ==  1:
		n[0] = n[0] + 1
	elif a[i] == 2:
		n[1] = n[1] + 1 
	elif a[i] == 3:
		n[2] = n[2] + 1 
	elif a[i] == 4:
		n[3] = n[3] + 1 
print(n)
 