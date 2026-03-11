altura_chico = 1.5
taxa_chico = 0.02
altura = float(input("Digite a altura a ser revisada: "))
taxa = float(input("Digite a taxa a ser utilizada: "))
ano = 0
while altura < altura_chico:
 altura_chico = altura_chico + taxa_chico
 altura = altura + taxa
 ano += 1
print(ano)