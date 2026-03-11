import math
vo = float(input("Digite a velocidade incial da flecha ao sair do arco em m/s: ")) # Declaração da velocidade inicial
d = float(input("Digite a distancia entre voce e o Falmer: ")) # Declaração da distancia
y = (math.asin(d*(9.8/(vo**2)))*(90/math.pi))
print(round(y,2))
