from numpy import *

n = array(eval(input("vetor de numeros:")))
v = ''

i = 0 
d = 0

while(i < len(n)):
	if (n[i] == "v"):
		d = d + 10 
	elif(n[i] == "face 2"):
		d = d + 5 
	elif(n[i] == "face 3"):
		d = d + 0
	elif(n[i] == "face 4"):
		d = d + 5
	elif(n[i] == "face 5"):
		d = d + 20 
	elif(n[i] == "face 6"):
		d = d + 10 
	i=i+1
print(n)