from numpy import *

vet = array(eval(input("Informe o tempo de chegada: ")))
var = min(vet)
k = var.index(vet)
print(k)