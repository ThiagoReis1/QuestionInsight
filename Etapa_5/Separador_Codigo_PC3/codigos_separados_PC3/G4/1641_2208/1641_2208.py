from numpy import*

tur=array(eval(input("Quantidade de Alunos: ")))

x=0

for i in range (size(tur)):
	if(tur[i]%3==0):
		x = x +1
	
vet=zeros(x, dtype = int)
print(x)
y=0
for i in range(size (tur)):
	if(tur[i]%3==0):
		vet[y]=i
		y=y+1
		
print(vet)

