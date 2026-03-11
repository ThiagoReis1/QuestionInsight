from numpy import *

vet = array(eval(input("Notas finais: ")))
ap = 0
ind = zeros(size(vet), dtype=int)

for i in vet:
	if i >= 5:
		ap = ap + 1
			
	
print(ap)
print(ind)