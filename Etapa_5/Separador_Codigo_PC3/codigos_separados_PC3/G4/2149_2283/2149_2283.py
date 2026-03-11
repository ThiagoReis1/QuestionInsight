from numpy import*
a = array(eval(input("Nota do ALUNO 1: ")))
b = array(eval(input("Nota do ALUNO 2: ")))
s = 0
apv = 0
for i in range(size(a)):
	if sum(a[i] + b[i]):
		s += 1
	if(sum(a[i]) >= 12) and sum(b[i] >= 12):
		ap += 1
vet = zeros(size(a), dtype=float)	
vet[0] = s
vet[-1] = apv
print(vet)
print(sum(vet))
	