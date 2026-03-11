from numpy import *

vet = eval(input("vet: "))
peso = array([5,4,3,2])

prod = dot(vet ,peso)
soma = dot(ones_like(peso), peso)
med = prod / soma

print(round(med,2))
