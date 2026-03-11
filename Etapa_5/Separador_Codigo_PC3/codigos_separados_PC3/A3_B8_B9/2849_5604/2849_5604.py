from numpy import*
notas=array(eval(input("notas: ")))
x=zeros(1,dtype=int)
soma=0

for i in notas:
	if i != 0:
		soma=soma+i
		x=soma
	elif i == 0:
		soma=0
print(x)
		