from numpy import*

vet = array(eval(input(" ")))
soro = zeros(4, dtype=int)
t1 = 0 
t2 = 0
t3 = 0
t4 = 0
for i in range(size(vet)):
	if vet[i] == 1:
		t1 = t1 + 1
	elif vet[i] == 2:
		t2 = t2 + 1
	elif vet[i] == 3:
		t3 = t3 + 1
	elif vet[i] == 4:
		t4 = t4 + 1
soro[0] = t1
soro[1] = t2
soro[2] = t3
soro[3] = t4
print(soro)
	