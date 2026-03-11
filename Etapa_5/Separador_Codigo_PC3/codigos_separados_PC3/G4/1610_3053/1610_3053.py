from numpy import*
s = input("String: ")
v = array(s.split(","))

i = 0
a = size(v)
vet = zeros(a)

while(i<size(v)):
	vet[i] = v[i]
	i = i + 1
a = sum(vet)
print(a)

