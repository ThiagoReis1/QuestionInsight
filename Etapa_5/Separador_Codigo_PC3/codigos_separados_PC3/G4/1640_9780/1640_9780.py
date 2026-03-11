from numpy import *
n = array(eval(input("insira qntt de aluno: ")))
impar = 0

for i in range (0, size (n)):
	if n [i] % 2 != 0 :
		 impar += 1 

ind = zeros (impar, dtype = int)
print(impar)

j= 0
for i in range (size(n)):
	if n [i] % 2 != 0:
		ind [j] = i 
		j += 1 
print(ind)