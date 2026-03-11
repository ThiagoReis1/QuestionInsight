#entradas

volume = (float(input("Valor consumido: ")))

#calculos

valor_da_conta = (volume * 0.37) + 15.0
valor2 = (valor_da_conta * 35) / 100 
valor3 = (valor_da_conta + valor2)

print(round(valor3, 2))