from numpy import *

rotulo = input().upper()
i = 0
custo = 0

while(i < len(rotulo)):
	if(rotulo[i] in ('A', 'E', 'I', 'O', 'U')):
		custo += 0.12
	else:
		custo += 0.18
	i += 1
	
print(round(custo, 2))