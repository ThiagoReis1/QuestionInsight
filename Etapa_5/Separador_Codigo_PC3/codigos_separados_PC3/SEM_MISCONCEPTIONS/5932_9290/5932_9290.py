tempo = float(input("tempo"))

minuto = 0.28
fixo = 23.00
icms= (31/100)

total = tempo * minuto + fixo + (tempo * minuto + fixo) * icms



print(round(total,2))