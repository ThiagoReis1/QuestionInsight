from numpy import*

face = array(eval(input("quantidade de lances: ")))

i = 0
pts = 0
					
while i < size(face):
		if face[i] == 1:
			pts += 10
		elif face[i] == 2:
		   pts += 5
		elif face[i] == 3:
			pts += 10
		elif face[i] == 4:
		   pts += 5
		elif face[i] == 5:
			pts += 10
		elif face[i] == 6:
			pts += 5
		i += 1
		
print(round(pts, 2))
		