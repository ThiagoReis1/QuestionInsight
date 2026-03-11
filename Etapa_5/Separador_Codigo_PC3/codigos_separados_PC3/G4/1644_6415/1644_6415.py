from numpy import*
media = array(eval(input("Digite a media dos alunos:")),dtype=int)
i = 0
soma = 0
for i in range(size(media)):
	if(media[i] < 5):
		soma = soma + 1		

a = zeros(soma, dtype=int)		
j = 0
for i in range(size(media)):
	if(media[i] < 5 ):
		a[j] = i
		j = j + 1
print(soma)
print(a)
	
	
	
	

	
	