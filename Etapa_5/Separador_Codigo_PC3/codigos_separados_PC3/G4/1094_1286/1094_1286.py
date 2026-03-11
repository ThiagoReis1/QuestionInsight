#Jose Carlos Gomes Pereira  21650882
#Data: 30/06/2016
#Avaliacao 02 Ex 02

x = int(input())
prop = ((x//1000)+(x%1000))**2

if x == prop:
 print(x, "atende a propriedade")
else:
 print(prop)