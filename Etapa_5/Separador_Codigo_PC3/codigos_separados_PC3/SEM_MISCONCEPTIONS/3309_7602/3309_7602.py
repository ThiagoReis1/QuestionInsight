
x = float(input("digite o peso da mercadoria: "))

quilo = x * 43.21
taxa = 25
total = quilo+taxa
imposto = total*(62/100)

total_final = total + imposto

print (round(total_final,2))