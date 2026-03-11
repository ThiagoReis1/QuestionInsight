from numpy import *

n = input("").upper()

B = 3.75
C = 7.90
E = 9.85
cont = 0
i = 0

while(i < size(n)):
	if n[i] == 'B' and n[i] == 'C' and n[i] == 'E':
		cont = B + C + E
	i = i + 1
print(round(cont, 2))
	