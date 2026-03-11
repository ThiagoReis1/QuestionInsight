from numpy import *
a = array(eval(input("insira: ")))
i = 0
s = 0
while(i<size(a)):
	if(a[i] == 1):
		s = s + 100
	elif(a[i] == 2):
		s = s + 60
	elif(a[i] == 3):
		s = s + 20
	elif(a[i] == 4):
		s = s 
	i += 1
print(s)