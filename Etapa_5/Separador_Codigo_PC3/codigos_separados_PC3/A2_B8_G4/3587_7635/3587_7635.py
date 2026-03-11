from numpy import*

v = array(eval(input("numero de aneis:")))
i = 100
l = 0
while(l < size(v)):
	if(v[l] == 1):
		i = i * 5
	elif(v[l] == 2):
		i =i * 3
	elif(v[l] == 3):
		i = i
	elif(v[l] == 4):
		i = i/2
	l = l + 1
print(round(i, 2))