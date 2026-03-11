import math
#variaveis
lado = int ( input ("Comprimento do lado: "))


#corpo
apm = lado / ( 2 * math.tan ( math.pi / 8 ))
Aoct = 4 * lado * apm


#mostrador
print ( round ( Aoct , 2 ))