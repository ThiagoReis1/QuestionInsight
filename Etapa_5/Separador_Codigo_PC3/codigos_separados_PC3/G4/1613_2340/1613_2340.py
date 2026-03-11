from numpy import*

vet1 = array(input("Atividade física; "))
vet2 = array(eval(input("Duração em min; ")))
vet1[0] = 3.0
vet1[1] = 10.3
vet1[2] = 6.7
vet1[3] = 9.7
vet1[4] = 5.0
kcal = vet1[0]*vet2[0]

print(kcal)