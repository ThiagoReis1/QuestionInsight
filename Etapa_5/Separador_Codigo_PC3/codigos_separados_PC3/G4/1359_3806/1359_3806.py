import math
ve= float(input("velocidade exaustiva do foguete: "))
mi= float(input("massa inicial: "))
mf= float(input("massa final: "))
V=ve* math.log(mi/mf)
print(round(V,2))