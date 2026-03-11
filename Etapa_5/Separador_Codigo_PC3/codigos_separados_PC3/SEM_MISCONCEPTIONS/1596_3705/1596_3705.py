from numpy import*
notas= array(eval(input()))
i=0
while i < size(notas):
	if(notas[i]) == min(notas):
		m=(sum(notas)- min(notas))/(size(notas) -1 )
	i = i +1
print(round(m,2))
	
		

