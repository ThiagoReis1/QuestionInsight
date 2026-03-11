from numpy import*
notas = array(eval(input("digite as notas:")))
pesos = [1,2,3]

soma = notas*pesos
soma1 = sum(soma)
soma2 = soma1/sum(pesos)
print(round(soma2,2))