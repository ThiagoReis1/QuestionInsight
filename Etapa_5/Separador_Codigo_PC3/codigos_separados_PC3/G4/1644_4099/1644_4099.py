from numpy import*

vet = array(eval(input("notas: ")))
sit = zeros(size(vet), dtype=int)
r = 0
for i in range(size(vet)):
	if(vet[i] < 5):
		r = r + 1
		sit[i] = i 

rep = zeros(r, dtype=int)
n = 0
for i in range(size(vet)):
	if(sit[i] > 0):
		n = n + 1
		rep[n] = i
print(r)
print(rep)