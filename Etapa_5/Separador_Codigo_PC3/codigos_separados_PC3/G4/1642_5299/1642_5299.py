from numpy import *
qa = array(eval(input("quantidade de alunos: ")))
cont = 0
for i in range(size(qa)):
	if (qa[i] % 5 == 0):
		cont = cont +1
print(cont)

j = 0
conx = zeros(cont, dtype=int)
for i in range(size(qa)):
	if (qa[i] % 5 == 0):
		conx[j] = i
		j = j+1
print(conx)
	