from numpy import*

n = array(eval(input("insira seu vetor: ")))
cont = 0
j = 0

for i in range(size(n)):
	if n[i] % 5 == 0:
		cont+=1
		
v = zeros(cont,dtype=int)

for i in range(size(n)):
	if n[i] % 5 == 0:
		v[j] = i
		j+=1

print(cont)
print(v)

	