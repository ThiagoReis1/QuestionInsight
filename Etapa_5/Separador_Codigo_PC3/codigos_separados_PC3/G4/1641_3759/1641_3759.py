from numpy import*
v = array(eval(input("Vetor:")))
t = 0

for i in range(size(v)):
	if(v[i]%3 == 0):
		t = t + 1
vet = zeros(t, dtype=int)
j = 0
for i in range(size(v)):
	if(v[i]%3 == 0):
		vet[j] = i
		j = j + 1
		
print(t)
print(vet)
	