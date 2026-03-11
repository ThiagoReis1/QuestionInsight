from math import*

angulo = float(input("Insira o angulo da flecha em graus:	"))
distancia =  float(input("Insira a distância em metros:	"))
gravidade = 9.8

velocidade = ((distancia * gravidade)/(sin(radians(2*angulo))) )** 0.5

print(round(velocidade,2))
