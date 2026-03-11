from numpy import*

vec = array(eval(input(": ")))

mat = zeros(4, dtype = int)

for i in range(size(vec)):
	if vec[i] == 1:
		mat[0] = mat[0] + 1
	elif vec[i] == 2:
		mat[1] = mat[1] + 1
	elif vec[i] == 3:
		mat[2] = mat[2] + 1
	elif vec[i] == 4:
		mat[3] = mat[3] + 1
		
print(mat)