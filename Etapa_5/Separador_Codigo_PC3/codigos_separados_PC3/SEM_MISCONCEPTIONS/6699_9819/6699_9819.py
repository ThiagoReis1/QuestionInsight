tempo = float(input("Insira o valor em horas"))

total = tempo * 15 + 5 
icms = total + 20/100 * total 
print(round(icms,2))

