from numpy import*

vet=array(eval(input("vetor de notas: ")))

soma=(sum(vet)-min(vet))
med=soma/(size(vet)-1)

print(round(med, 2))


