peso = float (input ("Digite o peso do saco de racao em gramas: "))
diaria = float (input ("Digite a quantidade diaria dada: "))


d = 5 * diaria
resto = peso - d


print (round(resto, 3))