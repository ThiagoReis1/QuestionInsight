
peso = float(input("Digite o peso do saco de racao: "))

qtd_diaria = float(input("Digite a quantidade diaria de racao: "))


consumo = peso - (qtd_diaria * 4) 



print(round(consumo, 2))