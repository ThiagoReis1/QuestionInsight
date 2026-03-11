from numpy import*
vn = array(eval(input("Qual o vetor notas?: ")))
vs = sum(vn) - min(vn)
med = vs / (size(vn) - 1)
print(round(med,2))