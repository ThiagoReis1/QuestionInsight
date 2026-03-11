taxa= 81/100
tfixa= 12.00
#ENTRADA DE DADOS 
encom= float(input("Digite o valor da encomenda: "))

#SAIDA VT= VALOR TOTAL, INCLUINDO TAXA DE IMPORTAÇÃO E TAXA FIXA

vt= encom+encom*taxa+tfixa
print(round(vt,2))