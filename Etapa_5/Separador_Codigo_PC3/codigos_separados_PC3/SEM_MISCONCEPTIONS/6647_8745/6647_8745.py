from numpy import*
notas = array(eval(input("Digite as notas: ")))
notas[0] = (notas[0] * 2)
notas[1] = (notas[1] * 1)
notas[2] = (notas[2] * 5)
notas_soma = (notas[0] + notas[1] + notas[2])
pesos_soma = 2 + 1 + 5
mpond = notas_soma/pesos_soma
print(round(mpond, 2))