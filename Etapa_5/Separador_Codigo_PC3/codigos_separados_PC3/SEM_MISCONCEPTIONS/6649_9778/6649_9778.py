from numpy import*

notas = array(eval(input('insira 5 notas: ')))
pesos = array ([3,2,4,1,3])

i=0
num=0

while i < size (notas):
	num += notas[i] * pesos [i]
	i+= 1

media = num/sum(pesos)
print(round(media,2))