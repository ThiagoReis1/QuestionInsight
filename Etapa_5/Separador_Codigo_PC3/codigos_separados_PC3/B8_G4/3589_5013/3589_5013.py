from numpy import*

n = array(eval(input(": ")))

i = 0
pt = 0
while i < size(n):
	if(n[i] == 1):
		pt = pt + 80
	elif(n[i] == 2):
		pt = pt + 40
	elif(n[i] == 3):
		pt = pt + 20
	elif(n[i] == 4):
		pt = pt + 10
	i = i + 1
print(pt)
	