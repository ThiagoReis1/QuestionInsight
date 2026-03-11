peso = float(input("peso do saco de racao: "))
qtd = float(input("quantidade: "))

semanal = qtd * 7
restante = peso - semanal

print(round(restante, 4))