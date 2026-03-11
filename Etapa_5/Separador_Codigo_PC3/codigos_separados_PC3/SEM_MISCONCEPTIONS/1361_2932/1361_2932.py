# Quantidade de pocoes
quantP = int(input())

# Ingredientes 
snow = float(((5 ** .5)- 1)/ 4) * quantP
saisF = float((5 - 2 *(5 ** .5))** .5) * quantP
aman = float(5 *(5 -(2 *(5 ** .5)))) * quantP

#Ingredientes necessarios
print(round(snow, 2))
print(round(saisF, 2))
print(round(aman, 2))