#Entrada de dados
p= float(input("Qual o preco da area por m2?"))
ap= float(input("Qual o tamanho da area privativa, em m2?"))
ac= float(input("Qual o tamanho da area comum, em m2?"))
ag= float(input("Qual o tamanho da area da garagem, em m2?"))

#Calculo Interno
s=ap+ac+ag
pt=s*p

#saida
print(round(pt, 2))