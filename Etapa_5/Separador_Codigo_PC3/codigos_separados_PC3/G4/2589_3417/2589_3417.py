from numpy import*
vet = array(eval(input("vetor: ")))

l = vet[0]
ls = l+(l*0.50)
m=0

for i in range(size(vet)):
	if vet[i]>ls:
		print(i)
		m = m + 1
print(m)
