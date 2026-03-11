#entrada
peso = float(input("qual o peso da mercadoria a ser transportada(em kg): "))

#valor do frete
aero = ((peso * 43.21) + 25)

#valor total, ja incluso impostos
imposto = ((62/100) * aero) + aero 

#saida
print(round(imposto, 2))