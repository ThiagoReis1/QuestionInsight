from numpy import*
from numpy.linalg import*

mat = array(eval(input("digite a matriz : ")))

a = zeros(shape(mat)[0], dtype = float)
b = 0
soma = 0
for i in range(shape(mat)[0]) :
	for j in range(shape(mat)[1]) :
		a[i] = min(mat[i,:])
for i in range(size(a)) :
	if a[i] == min(a) :
		print(i)


