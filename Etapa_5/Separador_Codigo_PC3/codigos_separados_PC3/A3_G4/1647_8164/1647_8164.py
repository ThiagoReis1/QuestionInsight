from numpy import*

freq = array(eval(input("digite as frequencias: ")))
aprov = 0

for i in range(size(freq)):
	if freq[i] >= 70:
		aprov = aprov + 1
		
pa = zeros(aprov, dtype=int)
pac = 0

j = 0
for x in range(size(freq)):
	if freq[x]>= 70:
		pa[j] = x
		j = j + 1
		
		
print(aprov)
print(pa)