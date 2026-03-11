v = float(input("informe o consumo em minutos"))
total = (v/0.28)+23
porcentagem = (v*31)/100
total = total+porcentagem
print("o valora a pagar é{:, 2f}" .format(total))


