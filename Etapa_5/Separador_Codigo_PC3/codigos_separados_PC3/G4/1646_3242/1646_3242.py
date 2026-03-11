from numpy import*

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: ")))
v = 0
for i in vet:
	if(i <= 50):
		v = v + 1
x = zeros(v, dtype = int)

v = 0
for j in range(size(vet)):
	if (vet[j]<= 50):
		x[v] = j
		v = v + 1
		
print(v)
print(x)
