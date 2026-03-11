from numpy import *

regis = array(eval(input()))
impar = 0
for i in range(len(regis)):
	if regis[i] % 2 != 0:
		impar += 1
		
impgrp = zeros(impar, dtype = int)
j = 0
for i in range(len(regis)):
	if regis[i] % 2 != 0:
		impgrp[j] = i
		j += 1
print(impar)
print(impgrp)