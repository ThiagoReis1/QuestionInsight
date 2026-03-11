#anotaçao 1:vetor que anote os andares
#anotaçao 4:preciso de uma equaçao para saber a diferença dos andares(como foi mostrado)
#anotaçao 2:vou precisar de um contador para as diferenças
#anotaçao 2.1:vou precisar de um contador para percorrer o vetor
#anotaçao 3:vai ter que fazer um while pegando o numero do verto e seu antecessor
from numpy import*
andar=array(eval(input("andares em que o elevador parou:")))
dif=0#vai armazenar os andares percorridos
i=0#vai percorer o meu vetor para fazer a equaçao funcionar
q=1#ele vai andar antes
while(i<size(andar) and q<size(andar)):#meu laço para fazer a equaçao
	if((andar[i+1]-andar[i])<0):#para mudar final
		dif = dif + (-1*(andar[q]-andar[i]))
	else:
		dif = dif + (andar[q]-andar[i])
	i=i+1
	q=q+1
print(dif)