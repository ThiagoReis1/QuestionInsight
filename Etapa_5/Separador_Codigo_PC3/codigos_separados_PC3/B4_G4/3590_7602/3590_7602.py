from numpy import*

face = array(eval(input()))
i = 0
cont = 0
while i < size(face):
	#face = array(eval(input()))
	if face[i] == 1:
		cont += 10
	elif face[i] == 2:
		cont += 5
	elif face[i] == 3:
		cont += 0
	elif face[i] == 4:
		cont += 5
	elif face[i] == 5:
		cont += 20
	else:
		cont += 10
	i += 1
	
print(cont)