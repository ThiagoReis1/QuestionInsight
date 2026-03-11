peso = float(input("Qual o peso do saco? "))
qtracao = float(input("Qual a quantidade diaria de racao? "))

qtsemana = qtracao*7

qtsaida = peso - qtsemana

print(round(qtsaida,2))