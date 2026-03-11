#José Carlos Gomes Pereira  -  21650882
#DATA: 16/06/2016
#Avaliação 01

min_exc = float(input())
min_exc = round(min_exc,2)

valor = (45 + (min_exc*0.97)) + ((45 + (min_exc*0.97))*0.42)

print(round(valor,2))