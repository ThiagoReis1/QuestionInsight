from numpy import*

pesos= ([1,3,2,5])
notas = array(eval(input('Digite 4 notas:')))

i=0
cont=0

while i < size(notas):
   cont += notas[i]*pesos[i]	
	
   i+=1
media = cont/sum(pesos)
print(round(media,2))