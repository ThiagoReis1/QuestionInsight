#Ingredientes
chifre = float(input("Gramas de chifre: "))
ouro = float(input("Gramas de ouro: "))
oleo = float(input("Gramas de oleo: "))

#Quantidade máxima de poções
pocoes_chifre = int(chifre/4.0)
pocoes_ouro = int(ouro/3.14)
pocoes_oleo = int(oleo/10.0)

#Valor mínimo
valor = min(pocoes_chifre, pocoes_ouro, pocoes_oleo)

print(valor)