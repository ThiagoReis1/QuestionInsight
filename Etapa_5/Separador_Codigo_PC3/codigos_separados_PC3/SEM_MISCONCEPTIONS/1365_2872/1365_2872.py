from math import*
g=9.8
angulo = float(input("Informe o valor do angulo da flecha"))
distancia = float(input("Qual e a distancia entre voce e o Falmer?"))
a = radians(angulo)
ang = sin(2*a)
v_inicial = float(sqrt(distancia*(g/ang)))
print (round(v_inicial,2))