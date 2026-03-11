from numpy import * 
q = array(eval(input("quantidade de alunos matriculados: ")))
ne = 0
for i in q:
	if(i % 5 == 0):
		ne = ne + 1 
print(ne)
a = zeros(ne, dtype = int)
x=0
y = 0
for i in q:
	if(i % 5 == 0):
		a[y] = x
		x = x + 1
		y = y + 1
	else:
		x = x + 1
print(a)