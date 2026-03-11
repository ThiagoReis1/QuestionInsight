peso_saco = float(input(" peso da racao em gramas: "))
quantidadediaria = float(input(" diaria das racoes: "))
quantidade_racao = peso_saco - quantidadediaria * 5
print(round(quantidade_racao, 2))
