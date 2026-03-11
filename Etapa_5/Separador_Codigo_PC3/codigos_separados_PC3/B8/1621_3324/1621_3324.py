from numpy import*
vetor1= array(eval(input().upper()))
vetor2= array(eval(input()))

i=0
soma=0
while(i<size(vetor1)):
	if(vetor1[i]=="ARROZ"):
		soma=soma + (vetor2[i]* 1.25)
	elif(vetor1[i]=="FEIJAO"):
		soma=soma + (vetor2[i]* 2.60)
	elif(vetor1[i]=="BIS"):
		soma=soma + (vetor2[i]* 1.80)
	elif(vetor1[i]=="MIOJO"):
		soma=soma + (vetor2[i]* 0.85)
	elif(vetor1[i]=="FANTA"):
		soma=soma + (vetor2[i]* 3.20)
	i=i + 1
print(round(soma,2))



		
	