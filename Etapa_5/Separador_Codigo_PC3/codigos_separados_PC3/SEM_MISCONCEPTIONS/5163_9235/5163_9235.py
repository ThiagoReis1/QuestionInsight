peso_do_saco = float(input("digite o peso em gramas: "))
quantidade_de_racao = float(input("digite a quantidade em gramas: "))

racoes_restantes = quantidade_de_racao * 5
x = peso_do_saco - racoes_restantes

print(round(x,  3))