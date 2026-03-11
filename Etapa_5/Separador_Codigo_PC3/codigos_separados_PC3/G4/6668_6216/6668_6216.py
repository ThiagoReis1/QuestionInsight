from numpy import *
x = array(eval(input("Precos dos materiais: ")))
y = 0
s = 0

for i in range(size(x)):
	if x[i] > 170:
		s = s+x[i]
		y+= 1
if y == 0:
	print(0.0)
else:
	media = s/y
	print(round(media, 2))
		
		
		
	

