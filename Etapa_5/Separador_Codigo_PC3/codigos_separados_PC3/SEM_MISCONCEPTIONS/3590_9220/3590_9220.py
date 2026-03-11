from numpy import *
face = array(eval(input()))

i = 0
total = 0

while i < size(face):
	if face[i] == 1 or face[i] == 6:
		total += 10
	if face[i] == 2 or face [i] == 4:
		total += 5
	if face[i] == 5:
		total += 20
	i += 1
	
print(total)
