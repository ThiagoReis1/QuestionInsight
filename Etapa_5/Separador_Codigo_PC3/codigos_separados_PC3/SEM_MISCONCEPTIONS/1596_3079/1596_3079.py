from numpy import*

notas = array(eval(input("Entre com as notas:")))
i=0

while(i < size(notas)):
	menor_nota = min(notas)
	media = (sum(notas) - menor_nota) /( size(notas) - 1)
	i = i + 1

print(round(media,2))	
	
	
	