from numpy import*

faces = array(eval(input("insira as faces do dado: ")))

pts = 0
i = 0 


while i < size (faces):
	if faces [i] == 1 or faces [i] == 3 or faces[i] == 5:
		pts = pts + 10
	elif faces [i] == 2 or faces [i] == 4 or faces [i] == 6:
		pts = pts + 5
		
	i += 1
	
print(pts)
	
	
	