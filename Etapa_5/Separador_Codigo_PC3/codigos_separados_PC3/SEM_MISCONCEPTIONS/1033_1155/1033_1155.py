peso= float(input("digite o peso"))
custo_frete= ((peso * 43.21) + 25)
valor= round(custo_frete * 62/100 + custo_frete,2)
print(valor)