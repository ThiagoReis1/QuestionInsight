from numpy import*

v = array(eval(input("notas:")))
i = 0
l = 0
while(l < size(v)):
	if(v[l] > 8):
		v[l] = 10
	elif(v[l] < 2):
		v[l] = 0 
	l = l + 1
print(v)