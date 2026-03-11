pop_inicial=int(input("Digite o número inicial de tracajás:"))
taxa_de_cresc=round(float(input("Digite a taxa de crescimento anual do número de tracajás:"))),2
qtd_roubada=int(input("Digite a quantidade de tracajás roubados"))
anos=int(input("Digite o número de anos:"))
pop=pop_inicial+(pop_inicial*taxa_de_cresc*anos)
pop_final=pop-qtd_roubada
print(pop_final)