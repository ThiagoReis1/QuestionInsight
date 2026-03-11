unid = input('informe a unidade de entrada (C)entimetro / (P)olegada: ').upper()
valor = float(input('qual o valor: '))

conversao = 0

if unid == "C":
    conversao = valor * 0.393701
else:
    if unid == "P":
      conversao = valor * 2.54

print(round(conversao,2))