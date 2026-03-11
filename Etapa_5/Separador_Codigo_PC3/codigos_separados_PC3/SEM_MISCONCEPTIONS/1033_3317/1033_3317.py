from math import*
peso = float(input("peso da mercadoria a ser transportada: "))
mercadoria = 43.21
taxa = 25.0
custodofrete = peso * mercadoria + taxa
imposto = custodofrete * 62/100
total = custodofrete + imposto
print(round(total, 2))

