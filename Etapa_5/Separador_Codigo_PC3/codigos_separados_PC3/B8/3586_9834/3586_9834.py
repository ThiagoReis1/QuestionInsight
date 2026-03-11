from numpy import *

aneis = array(eval(input("insira:")))

i = 0 
pts = 0

while i < size(aneis):
	if aneis[i] == 1:
		pts += 100
	elif aneis[i] == 2:
		pts += 60
	elif aneis[i] == 3:
		pts += 20
	elif aneis [i] == 4:
		pts += 0
	i += 1
	
print(round(pts, 2))
		
		