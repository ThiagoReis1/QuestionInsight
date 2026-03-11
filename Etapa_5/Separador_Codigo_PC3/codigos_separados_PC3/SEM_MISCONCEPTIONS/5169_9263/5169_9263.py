peso = float(input("digite o valor do peso em gramas do saco de racao: "))
quant = float(input("digite quantidade de racao ultilizada diariaente: "))
diario = quant*4
restante = peso - diario

print(round(restante,2))