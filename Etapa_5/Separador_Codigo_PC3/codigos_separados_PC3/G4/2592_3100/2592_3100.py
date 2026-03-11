from numpy import*
vet = array(eval(input()))
m = vet[0]
c = 1
t = 0
while(c < size(vet)):
	if(vet[c]>=m):
		t = t + 1
	c = c + 1
d = 1

while(d < size(vet)):
	if(vet[d]>=m):
		print(d)
	d = d + 1
print(t)