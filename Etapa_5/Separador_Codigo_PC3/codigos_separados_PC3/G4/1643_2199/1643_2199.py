from numpy import*

vet = array(eval(input("Notas dos alunos:")))

vcont = 0

for x in vet:
	if (x >= 5):
		vcont = vcont + 1
print(vcont)

cont = zeros(vcont, dtype=int)
c = 0
for i in range (size(vet)):
	if (vet[i] >= 5):
		cont[c] = i
		c = c + 1

print(cont)
		
