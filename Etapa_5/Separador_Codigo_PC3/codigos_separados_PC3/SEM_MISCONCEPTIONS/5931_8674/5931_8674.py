a = float(input('quantidade de minutos: '))

consumo = (a * 0.97) + 45

imposto = consumo*0.42 

total = consumo + imposto

print(round(total , 2))