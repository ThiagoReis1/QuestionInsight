#Entrada

peso = float(input("Digite o peso em gramas: "))
qtde = float(input("Digite a quantidade diaria em gramas: "))

#Expressão

resto = peso - qtde * 7

#Saída

print(round(resto, 3))