from numpy import *

face = array(eval(input("digite: ")))
pts = 0
i = 0

while i < size(face):
	if face[i] == 1:
		pts = pts + 10
	elif face[i] == 2:
		pts = pts + 5
	elif face[i] == 3:
		pts = pts + 0 
	elif face[i] == 4:
		pts = pts + 5
	elif face[i] == 5:
		pts = pts + 20 
	elif face[i] == 6:
		pts = pts + 10
	i = i + 1

print(sum(pts))