# guilherme silva almeida
plano_mensal = float(input("valor mensal:"))
minutos_excedente = float(input("minutos excedentes:"))
icms = float(input("icms:"))

custo = plano_mensal + minutos_excedente + icms
print(round(custo,2))
