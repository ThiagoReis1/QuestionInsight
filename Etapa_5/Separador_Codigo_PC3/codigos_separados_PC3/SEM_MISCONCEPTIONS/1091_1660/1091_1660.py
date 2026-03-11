####################################
# Universidade Federal do Amazonas
# Mauricio Naoto Handa Mitoso
# 30/06/2016
####################################

#definicao do numero
nro = int(input("Qual o numero? "))

parte_1 = nro // 100
parte_2 = nro % 100

if (((parte_1 + parte_2) ** 2) == nro):
	print(nro, "atende a propriedade")
else:
	print((parte_1 + parte_2) ** 2)
