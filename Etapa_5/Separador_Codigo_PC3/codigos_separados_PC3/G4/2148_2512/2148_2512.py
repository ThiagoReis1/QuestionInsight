from numpy import*

vet = array(eval(input()))

print(sum(vet))
ap = 0
for elemento in vet:
	if (elemento>=5):
		ap = ap + 1
print(ap)