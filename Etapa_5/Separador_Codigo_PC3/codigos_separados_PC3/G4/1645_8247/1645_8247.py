from numpy import*
vet = array(eval(input()))
c = 0

for i in range(size(vet)):
	if vet[i] >= 2000:
		c += 1

j = 0
vs = zeros(c, dtype=int)
for ch in range(size(vet)):
	if vet[ch] >= 2000:
		vs[j] = ch
		j += 1

print(c)
print(vs)