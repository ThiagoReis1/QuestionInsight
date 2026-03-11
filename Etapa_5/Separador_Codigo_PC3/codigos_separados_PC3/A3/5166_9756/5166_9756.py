pesagemracao = float(input("INFORME O PESO DO SACO DA RACAO (em gramas): "))
quantdiaria = float(input("QUANTAS (gramas) DE RACAO E FORNECIDA DIARIAMENTE?: "))

quantracao = pesagemracao/quantdiaria
fornecida = quantdiaria*5

restante = pesagemracao - fornecida

print(round(restante,2))
								  
								  