#para criar uma poção é ter proporção CERTA dos ingredientes
#ler snowberry
#quantidade máxima - menor razão disponibilidade

qtsnow = float(input())
qtsais = float(input())
qtamin = float(input())

snow = 0.31
sais = 0.73
amin = 2.64

val = min((qtsnow//0.31), (qtsais/0.73), (qtamin//2.64))
print(val)






