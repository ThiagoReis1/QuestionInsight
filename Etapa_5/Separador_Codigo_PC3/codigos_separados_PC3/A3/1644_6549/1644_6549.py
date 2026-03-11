from numpy import*

nf = array(eval(input("")))

aprov = 0
reprov = 0

for i in range(0, size(nf)):
	if nf[i] >= 5.0:
		aprov += 1
	else:
		reprov += 1
n_reprov = zeros(reprov, dtype=int)

acum = 0

for x in range(0, size(nf)):
	if nf[x] < 5.0:
		n_reprov[acum] = x
		acum += 1
		
print(reprov)
print(n_reprov)

