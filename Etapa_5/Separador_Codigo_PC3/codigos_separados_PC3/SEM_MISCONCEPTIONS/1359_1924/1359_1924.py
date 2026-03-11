from math import*
vel_ef = float(input("insira a velocidade de exaustão efeitiva"))
massai = float(input("insira a massa inicial do foguete"))
massaf = float(input("insira a massa final do foguete"))
calculo = vel_ef * log(massai/massaf) 
calculof = round(calculo,2)
print(calculof)