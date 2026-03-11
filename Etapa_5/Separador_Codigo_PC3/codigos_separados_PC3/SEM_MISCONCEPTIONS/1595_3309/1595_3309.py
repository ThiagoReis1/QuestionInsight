from numpy import *
vet = array(eval(input("insira: ")))
mfinal = (sum(vet) -min(vet))/(size(vet) - 1)
print(round(mfinal, 2))