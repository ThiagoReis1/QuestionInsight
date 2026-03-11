from numpy import*
vetor = array(eval(input("digite as distancias dos saltos: ")))
v = 0
l = 0
recorde = 8.95
while(v < size(vetor)):
	if(vetor[v] > recorde):
		l = l + 1
	v = v + 1
vet = zeros( size(vetor),dtype = float)
print(recorde)
print(l)