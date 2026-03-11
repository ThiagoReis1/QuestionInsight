from numpy import*
notas = array(eval(input("Digite as notas: ")))
pesos = [1, 2, 3]
i=0
num=0
den=0
while i < size(notas):
	num+=notas[i]*pesos[i]
	den+=pesos[i]
	i+=1
media=num/den
print(round(media,2))