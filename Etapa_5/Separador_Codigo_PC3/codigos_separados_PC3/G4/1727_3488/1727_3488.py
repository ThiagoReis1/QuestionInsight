from numpy import*
A = array(eval(input("Matriz:")))
b = zeros(shape(A)[0], dtype=float)

for i in range(shape(A)[0]):
	b[i] = max(A[i,:])

print(max(b))
	
	
	
	
