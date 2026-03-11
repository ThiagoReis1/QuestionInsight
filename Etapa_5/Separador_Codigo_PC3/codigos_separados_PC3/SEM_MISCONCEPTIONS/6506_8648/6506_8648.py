#Variáveis de entrada:
pratos_consumidos = int(input("Digite a quantidade de pratos consumidos: "))
s_n_sobremesa = input("Deseja sobrema sim (s) ou nao(n): ")
#Cálculo e condições:
if s_n_sobremesa == "s":
 valor_total = (40.00 * pratos_consumidos) - (40.00 * pratos_consumidos * 0.05)
 print(round(valor_total, 2))
if s_n_sobremesa == "n":
 valor_total = (40.00 * pratos_consumidos)
 print(round(valor_total, 2))