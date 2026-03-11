from math import*
angulo_flecha = radians(float(input("O angulo da flecha ao sair do arco em graus :")))
vel_inicial = float(input("Velocidade inicial da flecha ao sair do arco :"))
distancia = (vel_inicial**2) * ((sin(2 * angulo_flecha))/ 9.8)
print(round(distancia,2))
