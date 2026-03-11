from numpy import*
#vetor dos corredores tempo
tempos=array(eval(input("Tempo dos corredores")))
i=0#contador
#ult=max(tempos)#ferramenta de busca
while(i<size(tempos) and (tempos[i]!=max(tempos))):
	#if(tempos[i] != ult):
	i= i + 1 #para aumentar o contador
print(i)
		
