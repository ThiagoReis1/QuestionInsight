#Valor em pesos mexicanos (Variaveis de Leitura)
valor_mexicano = float(input("Digite o valor: "))
#Calculo valor em reais
valor_em_reais = valor_mexicano * 0.28
#Valor converito com duas casas decimais
print(round(valor_em_reais, 2))