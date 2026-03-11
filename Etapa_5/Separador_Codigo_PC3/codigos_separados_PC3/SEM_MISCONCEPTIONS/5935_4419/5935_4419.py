VALOR_POR_QUILO = 43.21
TAXA_FIXA = 25

pesoMercadoria = float(input("Qual o peso da mercadoria: "))
valorSemImposto = (pesoMercadoria * VALOR_POR_QUILO) + TAXA_FIXA
valorTotal = valorSemImposto + (valorSemImposto * .62)
print(round(valorTotal, 2))
