peso = float(input("Digite o peso do saco de racao em gramas: "))
qtd= float(input("Digite a quantidade diaria de racao em gramas: "))

semana = qtd * 7
resto = peso - (semana)

print(float(round(resto, 4)))