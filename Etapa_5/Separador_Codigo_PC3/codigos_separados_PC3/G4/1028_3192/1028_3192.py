vol1 = float(input("Volume de agua consumida durante o mes:"))

#Calculando o valor da conta+taxa
var1 = 15 + 0.37 * vol1

#Calculando o valor da conta+porcentagem
var2 = (var1 * 35) / 100

#Calculando valor total da conta+porcentagem
var3 = var1 + var2

print(round(var3, 2))