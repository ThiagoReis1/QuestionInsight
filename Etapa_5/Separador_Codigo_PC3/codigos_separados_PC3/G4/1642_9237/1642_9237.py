from numpy import*
vet = array(eval(input()))

t = 0
for i in range (size(vet)):
	if (vet[i] % 5 == 0):
		t = t + 1

v = zeros(t, dtype=int)
i = 0
for i in range (size(vet)):
	if (vet[i] % 5 == 0):
		v = v + 1
print(t)
print(v)