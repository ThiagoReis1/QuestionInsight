tempo = float(input("Informe o tempo de estacionamento:"))
gasto = tempo*15 + 5 + (tempo*15 + 5)*(20/100)

print(round(gasto, 2))