#quantidade de ingredientes necessario para preparar uma porcao
gramas_chifre_touro = 4.0
gramas_ouro_po = 3.14
gramas_de_oleo = 10.0

#leitura dos valores disponiveis
chifre_disponivel = float(input("Digite a quantidade de chifre de touro em gramas: "))
ouro_disponivel  = float(input("Digite a quantidade de ouro em po em gramas: "))
oleo_disponivel  = float(input("Digite a quantidade de oleo em gramas: "))

quantidade_porcao_de_chifre = chifre_disponivel // gramas_chifre_touro
quantidade_porcao_de_ouro =  ouro_disponivel // gramas_ouro_po
quantidade_porcao_de_oleo = oleo_disponivel // gramas_de_oleo

minima_razao = min(quantidade_porcao_de_chifre,quantidade_porcao_de_ouro, quantidade_porcao_de_oleo)

print(minima_razao)