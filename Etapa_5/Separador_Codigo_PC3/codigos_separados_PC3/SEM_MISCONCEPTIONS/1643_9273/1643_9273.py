from numpy import*

notas = array(eval(input(" :")))
# print(notas, type(notas))
aprovados = 0

for i in range(size(notas)):
	if notas[i] >= 5:
		aprovados = aprovados + 1
print(aprovados)
v = zeros(aprovados, dtype=int)
j = 0
for i in range(size(notas)):
	if notas[i] >= 5:
		v[j] = i
		j = j + 1

print(v)