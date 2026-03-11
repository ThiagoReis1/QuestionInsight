from numpy import *
medias = array([3,5,1], dtype=int)
notas = eval(input("notas: "))
soma_notas = sum(medias*notas)
soma_pesos = sum(medias)
media_ponderada = soma_notas/soma_pesos
print(round(media_ponderada,2))

