from numpy import*

vetor = array(eval(input("Digite as notas: ")))
peso = array([4,3])

total = sum(vetor * peso) / sum(peso)
print(round(total, 2))
