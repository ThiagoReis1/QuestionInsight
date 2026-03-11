from numpy import*

notas = array(eval(input("numeros")))
pesos = array([5,1])
num = notas * pesos
media = sum(num)/sum(pesos)
print(round(media,2))
				  
