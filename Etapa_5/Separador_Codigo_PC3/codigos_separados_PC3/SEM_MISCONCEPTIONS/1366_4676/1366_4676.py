from math import*
angulo= radians(float(input("o angulo da flecha ao sair do arco, em graus: ")))
velocidade= float(input("a velocidade inicial da flecha ao sair do arco, em metros por segundo: "))
g=9.8
d= velocidade**2*(sin(2*angulo)/g)

print(round(d, 2))

