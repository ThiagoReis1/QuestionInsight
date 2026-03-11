pesodoSaco = float(input("digite o peso do saco de racao: "))
quantdiaria = float(input("digite a quantidade diaria de racao: "))
consumosemana = quantdiaria * 7
quantrestante = pesodoSaco - consumosemana
print("quantidade restante no saco depois de uma semana: ")
print(round(quantrestante, 4))