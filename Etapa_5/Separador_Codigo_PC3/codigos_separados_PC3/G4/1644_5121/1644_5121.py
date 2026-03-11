from numpy import*
nota = array(eval(input("Informe as notas: ")))
i = 0
for a in nota:
	if(a<5):
		i = i + 1
v = zeros(i,dtype=int)
j = 0
k = 0
for b in nota:
	if(b<5):
		v[k] = j
		k = k + 1
	j = j + 1
print(i)
print(v)