#cambio real por dolar taxa fixa
taxa_fixa_servico = 12
dolar = 3.55
#quantia em reais
quantia = float(input("entre com o valor da quantia: "))
#quantia em dolares
quantia_dolares = (quantia - taxa_fixa_servico)/dolar
print(round(quantia_dolares, 2))