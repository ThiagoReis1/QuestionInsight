from numpy import*

face = array( eval ( input ("digite: ")))
p = 200
i = 0

while i < size(face):
	
	if face[i] == 1:
		p = p/2
	if face[i] == 2:
		p = p*3
	if face[i] == 3:
		p = p/2
	if face[i] == 4:
		p = p*3
	if face[i] == 5:
		p = p/2
	if face[i] == 6:
		p = p*3
		
	i = i + 1
		
print(round(p,2))