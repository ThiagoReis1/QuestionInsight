from numpy import*


vet=array(eval(input("vitimas: ")))
x=0

for i in range(1, size(vet)):
	if vet[i] >= vet[0]:
		print(i)
		x= x + 1
print(x)



