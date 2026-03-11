from numpy import*

tentativas=array(eval(input("numero de tentativas")))
pontuacao=100
ultimo=len(tentativas)-1
i=0

while(i<=ultimo):
	if(tentativas[i]==1):
	 pontuacao=pontuacao*5
	if(tentativas[i]==2):
	 pontuacao=pontuacao*3
	if(tentativas[i]==3):
	   pontuacao=pontuacao*1
	if(tentativas[i]==4):
	  pontuacao=pontuacao/2
	i+=1
pontuacao=round(pontuacao,2)
print(pontuacao)