from math import*
#ANGULO DA FLECHA AO SAIR DO ARCO EM GRAUS
a=radians(float(input("Qual é o valor do angulo em graus?")))
#DISTANCIA ENTRE VOCE E UMA CRIATURA FALMER, EM EMTROS
d=float(input("Qual é o valor da distancia?"))
#VALOR DA ACELERACAO DA GRAVIDADE
g=9.8
#CALCULO DA VELOCIDADE INICIAL (Vo)
Vo=sqrt(d*g/sin(2*a))
print(round(Vo,2))