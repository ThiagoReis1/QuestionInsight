# FRANCIANA DE SOUSA GOMES #

valenco = float(input())     #valor da encomenda
taxa = 12.00                 #taxa fixa
impos = (valenco * 81) / 100 #calculo do imposto de importação
#print(impos)

total  = valenco + taxa + impos
print(round(total, 2))