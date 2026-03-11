from numpy import*
pesos = [1,2,3]
notas = array(eval(input()))
				  
if size(notas) == size(pesos):
	media = 0
	pesos_x = 0
	i = 0
while i< size(notas):
		media = media + (notas[i] * pesos[i])
		pesos_x = pesos_x + pesos[i]
		i += 1
print(round(media/pesos_x, 2))