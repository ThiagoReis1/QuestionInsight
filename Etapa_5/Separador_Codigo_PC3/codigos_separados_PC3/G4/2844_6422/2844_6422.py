from numpy import*

mat = array(eval(input(": ")))

for i in range(len(mat)):
	if mat[i] == 0:
		mat[i] = 9
	else:
		mat[i] = mat[i] - 1
print(mat)