# Inserindo dados para a leitura da racao
peso = float(input("Qual o peso do saco de racao em gramas?: "))
qtde_diaria = float(input("Qual a quantidade diaria de racao em gramas?: "))

#Calculando a quantidade de racao resultante
qtde_final = peso - qtde_diaria * 5

#Imprimindo quantidade resultante
print(round(qtde_final, 2))