from math import *
n = int(input())
# Inicia variavel contadora
cont = 0
acm=1
# Inicia variavel acumuladora (primeiro termo da serie do PI)

# Imprime primeira aproximacao
soma=0
while (cont < n):
# Determina o denominador
    den = (6+acm+2)
# Computa novo termo da serie do PI
    soma = soma + ((-1) ** (acm+1) * 1. / den)
# Incrementa contador
    cont = cont + 1
    acm  = acm + 1
print(round(soma,8))
