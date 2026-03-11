#Instituto de Computacao - UFAM
#Lab 02 
#02/04/2018

#area se assemelha a um retangulo
#LEIA: LARGURA, COMPRIMENTO E CUSTO P/M**2
l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))
servico = float(input("Digite o custo do servico:  "))

#area do retangulo
area = l * c

#saida: custo total
ct = servico * (area)

print(round(ct,2))









