saco_racao = float(input("Qual o peso do saco de racao em gramas? "))
dose_diaria = float(input("Qual a quantidade diaria de racao em gramas? "))

restante_saco_racao = saco_racao - (dose_diaria*4)

print(round(restante_saco_racao, 2))