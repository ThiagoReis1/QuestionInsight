#constantes
gasolina = 2.86
oleo =  50.0
#quantidade de litros
quantidade = float(input("informe a quantidade de litros"))
#calculo
total = oleo + (quantidade * gasolina)
totalgeral = total * 0.34
#resultado
print (round(totalgeral,2))