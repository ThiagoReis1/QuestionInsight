from numpy import *
nota = array(eval(input("notas")))
soma = 0
x = size(nota)
for i in range(size(nota)):
	soma = soma + nota[i]
soma = soma - min(nota)
x = size(nota) - 1
me= soma/x
print(round(me,2))