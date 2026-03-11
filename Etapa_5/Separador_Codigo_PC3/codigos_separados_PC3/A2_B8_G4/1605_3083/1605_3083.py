from numpy import*
v = array(eval(input("circulos ")))
p = 200
t = 0
i = 0
while(t < 4):
	if(v[-1+i] == 1):
		p = p * 4
		t = t + 1
		i = i + 1
	elif(v[-1+i] == 2):
		p = p * 2
		t = t + 1
		i = i + 1
	elif(v[-1+i] == 3):
		p = p
		t = t + 1
		i = i + 1
	elif(v[-1+i] == 4):
		p = p/2
		t = t + 1
		i = i + 1
		
print(round(p, 2))