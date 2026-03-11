from math import*
velocidade= float(input("Diga a velocidade de exaustão efetiva em (m/s)"))
massa1= float(input("Diga a massa inicial do foguete: "))
massa2= float(input("Diga a massa final do foguete: "))

deltav = velocidade *(log(massa1/massa2))

print(round(deltav,2))