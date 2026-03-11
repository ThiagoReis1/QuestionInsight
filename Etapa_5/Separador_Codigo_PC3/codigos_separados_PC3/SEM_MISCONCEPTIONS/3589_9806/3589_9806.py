from numpy import *
aneis = array(eval(input("Anel acertado: ")))
i = 0
pts = 0 
while i < size(aneis):
	if aneis[i] == 1 :
		pts += 80
	if aneis[i] == 2: 
		pts += 40
	if aneis[i] == 3:
		pts += 20
	if aneis[i] == 4:
		pts += 10
	i += 1
print(pts)