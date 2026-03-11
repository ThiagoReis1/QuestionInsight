from numpy import *

p = array(eval(input("Precos: ")))
c = 0
p2 = 0

for i in range (size(p)):
	if p[i] >= 170:
		p2 = p2 + p[i]
		c += 1	
	media = p2/c
	print(round(media,2))
	else
	print("0.0")
		

		
