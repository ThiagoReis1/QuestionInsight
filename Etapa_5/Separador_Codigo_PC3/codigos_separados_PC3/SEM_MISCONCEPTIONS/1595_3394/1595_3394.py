from numpy import*
notas=array(eval(input("digite a nota:")))
i=0
j=0
while(i<size(notas)):
	if notas[i]<notas[j]:
		j=i
	i=i+1
	
	
media=((sum(notas)-notas[j])/(size(notas)-1))

print(round(media,2))
	