from numpy import* 

v = array(eval(input("")))

i = 0 
face = 0 

while(i<size(v)):
	if(v[i] == 1) or (v[i] == 3) or (v[i] == 5):
		face = 10 + face 
	elif(v[i] == 2) or (v[i] == 4) or (v[i] == 6):
		face = 5 + face 
	i+=1

print(face)
		