from numpy import *
x = array(eval(input("Vetor notas")))

k = (sum(x)-min(x))/(size(x)-1)
print(round(k,2))