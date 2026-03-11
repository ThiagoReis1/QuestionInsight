from numpy import *
face=array(eval(input("entre com os pontos: ")))
i=0
pontos=0
while (i<size(face)):
	if (face[i]==1):
		pontos+=10
	elif (face[i]==2):
		pontos+=5
	elif (face[i]==3):
		pontos+=10
	elif (face[i]==4):
		pontos+=5
	elif (face[i]==5):
		pontos+=10
	elif (face[i]==6):
		pontos+=5
	i+=1
print(sum(pontos))
		