from numpy import*

n = array(eval(input("vetor: ")))
conti = 0
b = 0


for i in n:
	if (i%2 != 0):
		conti = conti + 1
		
cont = zeros(conti, dtype=int)

for i in range(size(n)):
	if (n[i] % 2 != 0):
		cont[b] = i
		b = b + 1

	
print(conti)
print(cont)		