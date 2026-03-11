from numpy import*
vet  = array(eval(input("quantidade de alunos: ")))

n= size(vet)
x= 0
for i in range(n):
	if (vet[i] % 5 == 0):
		x = x + 1

s = zeros(x, dtype= int)
j= 0
for i in range(n):
	if (vet[i] % 5 == 0):
		s[j] = i 
		j= j + 1
		
print(x)
print(s)
	