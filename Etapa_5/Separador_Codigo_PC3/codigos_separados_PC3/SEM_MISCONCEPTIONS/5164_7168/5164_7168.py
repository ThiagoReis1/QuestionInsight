peso_saco = float(input("Qual o peso do saco de racao: "));
qtd_diaria = float(input("Qnt vc coloca de racao todo dia: "));
dias = int(4);
qtd_final = peso_saco - ((qtd_diaria) * dias);
print(round(qtd_final, 2))