from math import*
ve = float(input("digite a velocidade de exautao efetiva: "))
mo = float(input("digite a massa inicial do foguete: ")) #ncluindo o combustivel, em toneladas
mf = float(input(" digite a massa final do foguete: ")) # sem o combustivel, em toneladas
deltav = ve * log (mo/mf)
print(round(deltav, 2))