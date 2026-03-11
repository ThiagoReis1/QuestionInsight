from numpy import*

vet = array(eval(input("digite o cpf: ")))
vet_aux = array([9,8,7,6,5,4,3,2,1])
i = 0

total_soma =(vet[0]* vet_aux[0])+(vet[1]*vet_aux[1])+(vet[2]*vet_aux[2])+(vet[3]*vet_aux[3])+(vet[4]*vet_aux[4])+(vet[5]*vet_aux[5])+(vet[6]*vet_aux[6])+(vet[7]*vet_aux[7])+(vet[8]*vet_aux[8])
rtotal = total_soma % 11

print(rtotal)