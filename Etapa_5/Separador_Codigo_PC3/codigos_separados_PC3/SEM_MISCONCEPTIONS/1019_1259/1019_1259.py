#Julia Pacheco
#Av 01 - Ex01

#recebe largura e comprimento da fazenda, e o custo
largura = float(input("Digite o tamanho da largura: "))
comprimento = float(input("Digite o tamanho do comprimento: "))
custo = float(input("Digite o custo por m2: "))

#area da fazenda
area = largura * comprimento

#custo da aplicacao
custoTotal = area * custo

print(round(custoTotal,2))