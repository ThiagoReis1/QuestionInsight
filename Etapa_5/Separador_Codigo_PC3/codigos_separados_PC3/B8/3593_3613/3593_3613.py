from numpy import *

pontos = 200

faces = array(eval(input()))

i=0

while i<size(faces):
	if faces[i]>0 and faces[i]<7 and faces[i]%2 ==0:
		pontos = pontos*3
	elif faces[i] >0 and faces[i]<7:
		pontos = pontos/2
	i+=1
print(round(pontos,2))
		