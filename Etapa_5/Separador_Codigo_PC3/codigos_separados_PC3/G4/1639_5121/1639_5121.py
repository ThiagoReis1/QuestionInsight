from numpy import*
v = array(eval(input("Informe a quantidade de alunos matriculados: ")))
i = 0
j = 0
l = 0
x = []
for a in v:
	if(a%2==0):
		i = i + 1
		x.extend([j])
	if(j==0 and a%2==0):
		x.extend([0])
	j = j + 1
for b in x:
	if(b==0):
		del x[l]
	l = l + 1
print(i)
print(array(x))