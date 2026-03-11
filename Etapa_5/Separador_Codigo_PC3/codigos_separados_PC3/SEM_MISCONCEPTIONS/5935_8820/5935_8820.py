

peso = float(input("peso da mercadoria em kg: "))

frete = (43.21*peso) + 25 

imposto = 0.62 * frete

print(round(frete + imposto, 2))