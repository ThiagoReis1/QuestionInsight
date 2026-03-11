from numpy import*

x = array(eval(input("Faces: ")))

p = 200
i = 0 

while i < size(x):
	if x[i] == 1:
		p = p/2
	if x[i] == 2:
		p = p*3
	if x[i] == 3:
		p = p/2
	if x[i] == 4:
		p = p*3
	if x[i] == 5:
		p = p/2
	if x[i] == 6:
		p = p*3
		
	i += 1

print(round(p,2))
		