from numpy import* 

vetor = array(eval(input("vetor: ")))
pesos = array([3,2,4,1,3])
total = sum(vetor * pesos)/sum(pesos)

print(round(total, 2))
 