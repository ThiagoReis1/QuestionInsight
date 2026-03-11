from numpy import *
aneis = array(eval(input()))
i = 0 
pts = 10000

while i < size(aneis):
	if aneis[i] == 1:
		pts = pts * 2 
	elif aneis[i] == 3:
		pts = pts / 2 
	elif aneis[i] == 4:
		pts = pts / 4 
	i += 1	
print(round(pts, 2)) 