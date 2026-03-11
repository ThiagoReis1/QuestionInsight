from numpy import array
notas = array(eval(input()))
pesos = array([1,3,2,5])
m1 = notas[0]*pesos[0] + notas[1]*pesos[1] + notas[2]*pesos[2] + notas[3]*pesos[3]
m2 = pesos[0] + pesos[1] + pesos[2] + pesos[3]
m = m1/m2
print(round(m, 2))