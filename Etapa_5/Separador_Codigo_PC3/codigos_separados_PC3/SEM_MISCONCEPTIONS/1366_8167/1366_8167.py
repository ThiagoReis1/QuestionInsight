from math import *
angulo = radians(float(input("Digite o angulo da flecha ao sair do arco, em graus: ")))
velocidade_inicial = float(input("Digite a velocidade inicial da flecha ao sair do arco, em metros por segundo: "))
distancia = (velocidade_inicial)**2 * sin(2*angulo)/9.8
print(round(distancia,2))