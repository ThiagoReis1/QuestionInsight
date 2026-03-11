from numpy import*

vet= array(eval(input("VETOR: ")))

x = vet[1]
y = x+1
m =0

for i in range(size(vet)):
	if vet[i]>y:
		print(i)
		m= m +1
print(m)