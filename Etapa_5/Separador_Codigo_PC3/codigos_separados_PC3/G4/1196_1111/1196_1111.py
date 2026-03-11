from numpy import*
vetor=array(eval(input("Digite aqui o vetor:")))

i = 0
k = 0
while (i < size(vetor)):
	if (vetor[i] > 60 or vetor[i] < -60):
		k= k+1
	i= i+1

p=size(vetor)
num=p-k
vetor1=zeros(num, dtype=float)
a=0
b=0
while(a<p):
	if(vetor[a] > -60 and vetor[a] < 60):
		vetor1[b]=vetor[a]
		b = b + 1
	a=a+1
print(vetor1)