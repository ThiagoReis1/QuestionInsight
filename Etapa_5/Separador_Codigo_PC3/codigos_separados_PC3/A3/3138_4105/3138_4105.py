from numpy import*
vetor=array(eval(input("")))
i=0
soma=0
total=0
media=0
while(i<size(vetor)):
	soma=soma+(vetor[i]**7)
	i=i+1
total=soma/size(vetor)
media=total**(1/7)
print(round(media,2))