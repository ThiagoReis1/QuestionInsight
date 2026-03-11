from numpy import *
pts = 0
i = 0
dado = array(eval(input('face do dado: ')))
while(i < size(dado)):
	if(dado[i] == 1):
		pts += 10
	elif(dado[i] == 2):
		pts += 5
	elif(dado[i] == 3):
		pts = pts
	elif(dado[i] == 4):
		pts += 5
	elif(dado[i] == 5):
		pts += 20
	elif(dado[i] == 6):
		pts += 10
	i += 1
print(pts)