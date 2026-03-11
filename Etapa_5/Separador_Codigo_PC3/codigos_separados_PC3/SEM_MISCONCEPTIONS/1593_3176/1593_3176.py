from numpy import *

vn = array(eval(input('notas: ')))

qtd = size(vn)
qtd2 = size(vn) + 3

seq = arange(qtd, dtype=int) + 1
 

notastrab = vn * seq

mediatrabalho = sum(notastrab) / qtd2

print(round(mediatrabalho,2))
