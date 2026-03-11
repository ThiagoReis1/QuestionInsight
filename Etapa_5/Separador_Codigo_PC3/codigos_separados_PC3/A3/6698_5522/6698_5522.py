pedagio= 9.80
taxa= 20
icms= .15
pecas= float(input("quantidade de pecas: "))
valor= pecas*pedagio+taxa
total= valor + valor*.15
print(round(total, 2))