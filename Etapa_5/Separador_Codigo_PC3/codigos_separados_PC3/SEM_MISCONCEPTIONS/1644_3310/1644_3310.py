# aprovado nota>=5

from numpy import*

notas = array(eval(input("Digite a nota: ")))

contr = 0
conta = 0

for i in range(0,size(notas)):
	if(notas[i] < 5):
		contr = contr + 1
	else:
		conta = conta + 1
		
vet = zeros(contr,dtype=int)
c = 0

for i in range(0,size(notas)):
	if(notas[i]<5):
		vet[c] = i
		c = c + 1



print(contr)
print(vet)











