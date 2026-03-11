from numpy import *
nt = array(eval(input("notas: ")))

m = (sum(nt)-min(nt))/(size(nt)-1)

print(round(m,2))