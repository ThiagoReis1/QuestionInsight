from numpy import*

notas = eval(input("digite a nota: "))

pesos = array([5,4,3,2])

mediap = sum(notas*pesos)/sum(pesos)

mediap = round(mediap,2)

print(mediap)