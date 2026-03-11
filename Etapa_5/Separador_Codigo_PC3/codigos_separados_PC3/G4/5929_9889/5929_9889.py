# agua = 0.37 + fixo de 15 
# aplicado um aumento de 35 %

va = float(input("Digite o volume de agua consumida em certo mes: "))

vp = ((va * 0.37) + 15) * (1+0.35)

print(round(vp,2))