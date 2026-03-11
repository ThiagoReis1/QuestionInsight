from numpy import*
v = array(eval(input("Faces: ")))

i = 0
t = 0
while(i < size(v)):
	if(v[i] == 1):
		p = 10
	elif(v[i] == 2):
		p = 5
	elif(v[i] == 3):
		p = 10
	elif(v[i] == 4):
		p = 5
	elif(v[i] == 5):
		p = 10
	elif(v[i] == 6):
		p = 5
	t = t + p
	i = i + 1
print(t)
	
		
	