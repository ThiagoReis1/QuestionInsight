from numpy import*

notas = array(eval(input("digite as notas: ")))
pesos = ([4,3])

total = sum(notas * pesos) / sum(pesos)

print(round(total, 2))