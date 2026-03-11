animais = 3 #animais alimentados por dia
dias = 7 #Dias da semana
peso = float(input("Peso em gramas do saco: "))
qtd = float(input("Consumo diario de racao: "))

sobra = (peso - (qtd * dias)) #Calculo da sobra de racao

print(round(sobra, 3))


