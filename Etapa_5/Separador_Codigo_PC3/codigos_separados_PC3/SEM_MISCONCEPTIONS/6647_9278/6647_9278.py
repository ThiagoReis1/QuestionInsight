from numpy import*

notas = eval(input("digite o vetor de notas: "))

pesos = array([2,1,5])

m_ponderada = sum(notas * pesos) / sum(pesos)

print(round(m_ponderada,2))