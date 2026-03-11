from numpy import*

vet =  array(eval(input("vetor: ")))
n = int(input("n: "))

i = 0
c = 0

while i < size(vet):
	if n > vet[i]:
		c = c + 1
	if n == vet[i]:
		print(i)
	i = i + 1
	
print(c)