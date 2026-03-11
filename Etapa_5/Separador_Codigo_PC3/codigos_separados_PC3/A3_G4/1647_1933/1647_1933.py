from numpy import*
v = array(eval(input("frequencias:")))
ap = 0
i = 0
a = 0
vet = arange(ap)
while(i < size(v)):
	if(v[i] >= 70):
		ap = ap + 1
	i = i + 1
vet = arange(ap)

while(a < size(v)):
	if(v[a] >= 70):
		for x in range(size(vet)):
			vet[x] = v[a]
			
		
	

print(ap)
print(vet)
#print(vet)