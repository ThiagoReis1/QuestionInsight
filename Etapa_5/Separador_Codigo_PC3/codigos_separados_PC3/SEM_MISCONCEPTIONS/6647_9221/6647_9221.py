from numpy import*

notas = array (eval (input (" digite as notas: ")))
pesos = [2, 1, 5]

media_ponderada = dot(notas, pesos)/ sum(pesos)

print (round (media_ponderada, 2))
