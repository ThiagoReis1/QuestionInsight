from numpy import *
n = array(eval(input("Notas: ")))

m = (sum(n) - min(n))/(size(n) - 1)
print(round(m, 2))