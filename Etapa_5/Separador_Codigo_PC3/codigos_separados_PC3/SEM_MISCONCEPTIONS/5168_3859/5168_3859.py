#Racao para Papagaio


peso = float(input("Qual a quantidade do saco de racao em gramas?"))
rac = float(input("Qual a quantidade de racao diaria em gramas?"))

quantidade = rac*7
total = peso - quantidade

print (round(total,4))

