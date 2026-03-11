from numpy import *
nota= array(eval(input("Digite as notas: ")))

cont= 0

for i in range(size(nota)):
	if nota[i] < 5.0:
		cont= cont + 1

v= zeros(cont, dtype=int)

cont1= 0
for i in range(size(nota)):
	if nota[i] < 5.0:
		v[cont1]= i
		cont1= cont1 + 1

print(cont)
		
print(v)