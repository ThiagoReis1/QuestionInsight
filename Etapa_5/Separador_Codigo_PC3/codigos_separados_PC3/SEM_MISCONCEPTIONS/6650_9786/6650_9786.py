from numpy import * 

notas = array(eval(input('insira 2 notas:')))
pesos = array ([4,3])

num = notas * pesos
media = sum(num)/sum(pesos)
print(round(media,2))