from math import * 

#Programa pra ler massa
p = float(input("massa da espada: "))

#Gramas de flawless ruby
fr = 2**(1+p/1000)
print(round(fr,2))

#Gramas de soul gem
sg = p * pi**2 / 3141
print(round(sg,2))

#Gramas de oleo de dwarven
od = 2 * sqrt(p/40)
print(round(od,2))

