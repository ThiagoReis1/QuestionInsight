num = float(input("Escreva um numero de  8 digitos: "))
num1 = num / 10000000
resto1 = num % 10000000
num2 = resto1 / 1000000
resto2 = resto1 % 1000000
num3 = resto2 / 100000
resto3 = resto2 % 100000
num4 = resto3 / 10000
resto4 = resto3 % 10000
num5 = resto4 / 1000
resto5 = resto4 % 1000
num6 = resto5 / 100
resto6 = resto5 % 100
num7 = resto6 / 10
resto7 = resto6 % 10
num8 = resto7 / 1
resto8 = resto7 % 1

num1 = (int(num / 10000000))
num2 = (int(resto1 / 1000000))
num3 = (int(resto2 / 100000))
num4 = (int(resto3 / 10000))
num5 = (int(resto4 / 1000))
num6 = (int(resto5 / 100))
num7 = (int(resto6 / 10))
num8 = (int(resto7 / 1))
x1 = (num1*1000+num2*100+num3*10+num4*1)
x2 = (num5*1000+num6*100+num7*10+num8*1)
if((x1+x2)**2 == num):
	print(num,"atende a propriedade")
else:
	print((x1+x2)**2)	