from numpy import *

face = array(eval(input("face do dado: ")))
i = 0
total = 0

while i < size(face):
	if face[i] == 1:
		total += 10.00
	elif face[i] == 2:
		total += 5.00
	elif face[i] == 4:
		total += 5.00
	elif face[i] == 5:
		total+= 20.00
	elif face[i] == 6:
		total += 10.00
	i += 1

print(round(total,2))