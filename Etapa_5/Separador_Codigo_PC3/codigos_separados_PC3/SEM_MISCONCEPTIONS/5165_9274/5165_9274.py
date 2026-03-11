peso = float(input("Qual o peso?"))

qtd_diaria = float(input("Quanto e consumido diariamente?"))

dias = 6

racao_apos6dias =  peso - qtd_diaria * dias

print(round(racao_apos6dias,4))