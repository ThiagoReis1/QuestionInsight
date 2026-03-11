from numpy import*

x = array(eval(input("Digite as notas: ")))

i = 0

t = []

while i < size(x):
	if x[i] > min(x):
		t.append(x[i])
	i += 1
Mfinal = (x[0]*2 + x[1]*3 + x[2]*5)/10
print(round(Mfinal, 2))

if Mfinal >= 5:
	print("APROVADO")
else:
	print("REPROVADO")


