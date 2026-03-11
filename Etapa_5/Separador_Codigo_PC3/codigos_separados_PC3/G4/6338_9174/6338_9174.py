from numpy import *

x= array(eval(input("vetor: ")))
y = int(input("numero inteiro: "))
i = 0
w =0
while i < size(x):
	if x[i] == y:
		print(i)
		
	
	if x[i] > y:
		w = w +1
	i = i + 1
print(w)

	

	