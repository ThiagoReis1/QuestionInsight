from numpy import*
vent = array(eval(input()))
vsai = array(eval(input()))

vet0 = vent[0] - vsai[0]
vet1 = vent[1] - vsai[1]
vet2 = vent[2] - vsai[2]
vet3 = vent[3] - vsai[3]

vt = vet0 + vet1 + vet2 + vet3
print(vt)