#UNIVERSIDADE FEDERAL DO AMAZONAS
#ICC  ---- 30/06/2016
#AVALIAÇÃO 2 ----- exercicio 2
#MATHEUS GABRIEL PEREIRA DE CAMPOS

num=int(input("Digite o numero desejado:"))

num1=num//100000
resto1=num%100000
num2=resto1//10000
resto2=num%10000
num3=resto2//1000
resto3=num%1000
num4=resto3//100
resto4=num%100
num5=resto4//10
resto5=num%10
num6=resto5//1
resto6=num%1

s=(((num1*100+num2*10+num3)+(num4*100+num5*10+num6))**2)
if num==s:
	print( num, "atende a propriedade")
else:
	print(s)
