peso_do_saco = float(input('peso(g) do saco de racao: '))
qdiaria = float(input('quantidade de racao(g) por dia: '))
resto = peso_do_saco - qdiaria * 7
print(round(resto,3))