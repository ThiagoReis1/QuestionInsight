from numpy import*

notas = array(eval(input(': ')))

med = (sum(notas)-min(notas))/(size(notas) - 1) 

print(round(med, 2))