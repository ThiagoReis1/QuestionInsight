from numpy import*

nota = array(eval(input("Notas: ")))
vet = (sum(nota) - min(nota))/ (size(nota) - 1)
print(round(vet, 2))