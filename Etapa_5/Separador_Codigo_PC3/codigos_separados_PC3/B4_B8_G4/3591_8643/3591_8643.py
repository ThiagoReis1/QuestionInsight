from numpy import*

vt = array(eval(input()))
i = 0 
o = 0

while(i < size(vt)):
	if(vt[i] == 1):
		o = o + 10
	elif(vt[i] == 2):
		o = o + 5
	elif(vt[i] == 3):
		o = o + 10
	elif(vt[i] == 4):
		o = o + 5
	elif(vt[i] == 5):
		o = o + 10
	elif(vt[i] == 6):
		o = o + 5
	i = i + 1
print(o)
