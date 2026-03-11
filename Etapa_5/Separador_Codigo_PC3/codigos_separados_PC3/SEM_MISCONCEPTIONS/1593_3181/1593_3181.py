from numpy import*
notas = array(eval(input("")))
i = 0
peso = 1
media = 0
sum_peso = 0
while(i < size(notas)):
	media = notas[i]*peso + media
	sum_peso = sum_peso + peso
	peso+=1
	i+=1
media = media/sum_peso
print(round(media,2))

