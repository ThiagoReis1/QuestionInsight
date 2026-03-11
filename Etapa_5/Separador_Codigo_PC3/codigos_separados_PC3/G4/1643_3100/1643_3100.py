from numpy import*
notas = array(eval(input()))
ap = 0
c = 0
while(c < size(notas)):
	if(notas[c]>=5):
		ap = ap + 1
	c = c + 1
vet = zeros(ap, dtype=int)
c = 0
p = 0
while(c < size(notas)):
	if(notas[c]>=5):
		vet[p]=c
		p = p + 1
	c = c + 1
print(ap)
print(vet)
