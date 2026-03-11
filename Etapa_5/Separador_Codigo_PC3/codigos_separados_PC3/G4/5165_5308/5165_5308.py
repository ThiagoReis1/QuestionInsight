peso = float(input("peso da racao(em gramas): "))

quant_d = float(input(" quantidade diaria de racao em gramas: "))

dias = quant_d * 6

apos = peso - dias

print(round( apos , 4))