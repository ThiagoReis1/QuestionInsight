from math import*
largura = float(input ("Digite a largura: "))
comprimento = float(input ("Digite o comprimento: "))
custo_m2 = float(input("Digite o custo da aplicacao do fungicida"))

custo_total = float ( largura * comprimento * custo_m2)

print (round( custo_total , 2))

