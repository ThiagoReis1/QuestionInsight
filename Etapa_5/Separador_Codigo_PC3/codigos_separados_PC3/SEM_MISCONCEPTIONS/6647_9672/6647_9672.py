from numpy import*

notas= array(eval(input("Insira as notas: ")))
peso= array([2,1,5])

i= 0 
soma= 0 

while (i < size(notas)):
	soma= soma + notas[i] * peso[i]
	i= i + 1
	media= soma / sum(peso)
	
print(round(media,2))