#conta = (0,43 por kwh + 10)*1,25 arredondado em duas casas decimais
potencia = float(input("Quantos kwh o individuo consumio? "))
valor = ((0.43*potencia)+10)*1.25
print(round(valor, 2))
