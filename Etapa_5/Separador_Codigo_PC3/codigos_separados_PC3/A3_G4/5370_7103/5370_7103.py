from numpy import *
V = array(eval(input("Vetor: ")))
i = 0
a = "True"
while i<size(V)-1:
	if V[i]>=V[i+1]:
		a = "False"
	i = i + 1
	

print(a)
