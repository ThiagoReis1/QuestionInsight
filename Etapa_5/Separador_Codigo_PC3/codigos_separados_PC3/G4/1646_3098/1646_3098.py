from numpy import*
#vetor de entrada
val=array(eval(input("valor dos saques:   ")))
#contadoras
saqb=0   #saques abaixo do limite de 50 reais
j=0  		#controla a posiçao do vetor de entrada
k=0		#controla o vetor de saida(iniciar fora fora do segundo laço, mas atualiza ele.)
saqn=0
for i in range(size(val)):	#começo do meu primeiro laço de verificaçao
	if(val[i]<=50):
		saqb = saqb + 1
		
	else:###isso é só para me guiar na ideia
		saqn = saqn + 1
		

#criando o vetor de saida
saida=zeros(saqb,dtype=int)

#meu segundo laço
for i in range(size(val)): #vamos começar a fazer a resposta
	#atribuindo valor a saida
	if(val[i]<=50):
		saida[j] = i
		j = j + 1
	else:
		k = k + 1
print(size(saida))
print(saida)
