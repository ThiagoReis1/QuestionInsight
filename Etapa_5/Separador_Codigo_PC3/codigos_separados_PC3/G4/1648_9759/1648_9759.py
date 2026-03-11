from numpy import*

a  = array(eval(input("Informe o vetor: ")))

c = 0
for i in range(size(a)):
	if a[i] < 70:
		c = c + 1
print(c)

vetor = zeros(c, dtype = int)
j = 0
for i in range(size(a)):
	if a[i] < 70:
		vetor[j] = i 
		j = j + 1 
print(vetor)
	
	
		