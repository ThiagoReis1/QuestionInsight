from numpy import*

vetor = array(eval(input(" : ")))
pesos = array([5,1])
total = sum(vetor*pesos)/sum(pesos)

print(round(total, 2))