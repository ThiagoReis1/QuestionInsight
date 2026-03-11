from numpy import *
vet_banho = array(eval(input()))
vet_perc = array(eval(input()))
cons = sum(vet_banho//vet_perc)
print(round(cons, 2))

