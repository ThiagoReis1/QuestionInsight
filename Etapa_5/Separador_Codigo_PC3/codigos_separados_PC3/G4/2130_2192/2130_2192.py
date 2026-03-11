from numpy import *

n = array(eval(input())) 

i = 0
c = 0

while(i < size(n)):
	if(i == 0):
		c = c + n[0]*3.0
	if(i == 1):
		c = c + n[1]*2.0
	if(i == 2):
		c = c + n[2]*2.0
	if(i == 3):
		c = c + n[3]*3.0
	i = i + 1
	
m = round((c/10.0), 2)

print(m)

if(m >= 5):
	print("APROVADO")
else:
	print("REPROVADO")
		