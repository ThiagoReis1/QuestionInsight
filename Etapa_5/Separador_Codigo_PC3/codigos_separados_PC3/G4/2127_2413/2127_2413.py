from numpy import *

x= array(eval(input("Digite as notas: ")))

i = 0
t = []
while i < size(x):
	if x[i] > min(x):
		t.append(x[i])
	i += 1
	
Mfinal = (sum(t)/3)
print(round(Mfinal,2))

if Mfinal >= 50:
	print("APROVADO")
else:
	print("REPROVADO")
