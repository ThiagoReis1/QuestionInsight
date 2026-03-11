# Ler o ângulo da fecha em graus e a distância em metros
import math 

a = float (input ("Qual o ângulo da flecha?"))
a = math.radians (a)
d = float (input ("Qual a distância?"))

g= 9.8

v = (math.sqrt ((d*g)/math.sin(2*a)))

print (round (v,2))