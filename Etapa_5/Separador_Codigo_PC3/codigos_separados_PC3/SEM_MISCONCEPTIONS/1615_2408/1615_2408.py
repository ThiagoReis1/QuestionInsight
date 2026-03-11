from numpy import *

v = array(eval(input("primeiro jogador")))
v1 = array(eval(input("segundo jogador")))

c = 0
i = 0

while(i < size(v)):
	if(v[i] == 1):
		c = c + 40
	if(v[i] == 2):
		c = c + 20
	if(v[i] == 3):
		c = c + 10
	if(v[i] == 4):
		i = i + 1 
	else:
		print("JOGADOR UM")
	else:
		print("JOGADOR DOIS")
print(c)
	
	
	
