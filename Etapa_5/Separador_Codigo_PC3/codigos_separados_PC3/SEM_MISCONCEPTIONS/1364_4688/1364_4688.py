from math import*

velocidade = float(input("velocidade inicial da flecha ao sair do arco: "))
distancia = float(input("distancia entre voce e o Falmer: "))

from math import*

angulo = asin(distancia*9.8/velocidade**2)*90/pi

print(round(angulo, 2))

