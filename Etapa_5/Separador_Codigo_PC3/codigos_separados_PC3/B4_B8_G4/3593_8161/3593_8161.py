from numpy import *
n = array(eval(input("numero:")))
p = 200
i = 0
while i<len(n):
	if n[i] == 1:
		p=p/2
	elif n[i] == 2:
		p=p*3
	elif n[i] == 3:
		p=p/2
	elif n[i] == 4:
		p=p*3
	elif n[i] == 5:
		p=p/2
	elif n[i] == 6:
		p=p*3
	i = i+1
print(round(p, 2))
		
		