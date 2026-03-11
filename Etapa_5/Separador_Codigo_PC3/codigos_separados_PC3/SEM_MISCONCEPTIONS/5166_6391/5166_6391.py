peso_do_saco = float(input("Determine um peso em gramas para o saco: "))

quantidade_diaria = float(input(" Determine a quantidade diaria: "))

resto_de_racao = peso_do_saco - ( quantidade_diaria * 5 )

print(round(resto_de_racao, 2))