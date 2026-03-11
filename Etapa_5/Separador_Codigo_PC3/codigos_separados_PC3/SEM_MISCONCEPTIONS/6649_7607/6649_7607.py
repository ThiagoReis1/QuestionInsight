from numpy import*
vetor = array(eval(input("Digite as notas: ")))

peso = (3,2,4,1,3)

soma_ponderada = sum(vetor * peso)
pesos = sum(peso)

media_ponderada = soma_ponderada / pesos

print(round(media_ponderada,2))