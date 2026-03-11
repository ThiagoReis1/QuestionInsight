min = float(input("Digite os minutos excedentes: "))
minex = 0.97
mensal = 45
plano = mensal + minex * min 
percentual = 0.42
valor = plano + plano * percentual
print(round(valor, 2))
