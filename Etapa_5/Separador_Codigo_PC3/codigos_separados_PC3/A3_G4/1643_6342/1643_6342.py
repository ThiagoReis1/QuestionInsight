from numpy import *

v = array(eval(input("alunos que passaram: ")))
ac = 0
for i in range (size(v)):
	if v[i] >= 5:
		ac = ac +1
v1 = zeros(ac, dtype=int)
cont = 0
for i in range (size(v)):
	if v[i] > 5:
		v[cont] = i
		cont = cont + 1
	
print(ac)
print(v)