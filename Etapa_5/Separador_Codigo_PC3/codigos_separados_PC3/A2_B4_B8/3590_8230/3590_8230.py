from numpy import *

faces = array(eval(input("informe as faces do dado sorteadas pelo jogador: ")))
total = 0
i = 0

while i < size(faces):
	face = faces[i]
	
	if(face == 1):
		total = total + 10
	elif(face == 2):
		total = total + 5
	elif(face == 3):
		total = total
	elif(face == 4):
		total = total + 5
	elif(face == 5):
		total = total + 20
	elif(face == 6):
		total = total + 10
		
	i = i + 1
	
print(total)