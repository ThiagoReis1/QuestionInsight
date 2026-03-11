from math import * 

a = radians( float(input("Digite o angulo da flecha ao sair do arco, em graus: ")))
d = float(input("Digite a distancia entre voce e uma criatura falmer, em metros: "))

calculo = sqrt( d * (9.8 / sin(2*a)))

print (round(calculo,2))