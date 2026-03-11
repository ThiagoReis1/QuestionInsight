#  Universidade Federal do Amazonas
#  Aluno: Micael Davi Lima de Oliveira - 21851626
#    
#  Questão 2: O programa deverá calcular a média aritmética
#	   	     de 4 alturas(dadas em metros), sendo que no
#			     fim a média deve ser impressa com um arren-
#				  dondamento de 2 casas decimais.

alt1 = float(input("1. Por favor, insira a altura(m) do (Primeiro) integrante do grupo: "))
alt2 = float(input("2. Por favor, insira a altura(m) do (Segundo) integrante do grupo: "))
alt3 = float(input("3. Por favor, insira a altura(m) do (Terceiro) integrante do grupo: "))
alt4 = float(input("4. Por favor, insira a altura(m) do (Quarto) integrante do grupo: "))

media = (alt1 + alt2 + alt3 + alt4) / 4
print(round(media, 2))