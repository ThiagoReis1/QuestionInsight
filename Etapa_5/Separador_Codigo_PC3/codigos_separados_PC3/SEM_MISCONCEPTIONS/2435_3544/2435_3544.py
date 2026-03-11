# ------------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# THIAGO ANDRADE DOS SANTOS
# DATA: 02/04/2018
#
# OBJETIVO: Calcular o cambio do peso argentino 
#-------------------------------------------------------------
preco = float(input("preco_produto = "))
desconto = preco*0.4
preco_com_desconto = preco - desconto
taxa_entrega = preco*0.05
print(round(preco_com_desconto,2))
print(round(taxa_entrega,2))
