from numpy import*
freq = array(eval(input()))
reprov = 0
for i in range(0,size(freq)):
	if freq[i] >= 0 and freq[i] < 70:
		reprov += 1
aux = zeros(reprov, dtype = int)
j = 0
for i in range(0,size(freq)):
	if freq[i] < 70:
		aux[j] = i
		j +=  1
print(reprov)
print(aux)