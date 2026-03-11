from numpy import *
n = array(eval(input()))
soma = sum(n)
soma = soma - min(n)
media = soma/(size(n)-1)
print(round(media, 2))