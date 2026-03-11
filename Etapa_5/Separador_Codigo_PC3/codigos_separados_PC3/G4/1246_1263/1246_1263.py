from numpy import*

v=float(array(eval(input())))
x=array(zeros(2, dtype=int))
A=min(v)
B=max(v)
C=( 0.75*A + 0.25*B )
D=(0.25*A + 0.75*B)
soma=0
for i in range(size(v)):
	if(A<=[i]and [i]< C):
		soma=soma + 1
		x[0]=soma

soma=0
for i in range(size(v)):
	if(C <= [i]and [i]< D):
		soma=soma + 1
		x[1]=soma
print(x)

