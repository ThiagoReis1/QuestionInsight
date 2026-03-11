numero = (float(input("Escreva um numero de 4 digitos: ")))
num1 =  num / 1000
resto_num1 = num % 1000
num2 = resto_num1 / 100
resto_num2 = resto_num2 % 100
num3 = resto_num2 / 10
resto_num3 = resto_num2 % 10
num4 = resto_num3 / 1
resto_num4 = resto_num3 % 1
soma = num1 + num2 + num3 + num4

num1 = (int(num / 1000))
num2 = (int(resto_num1 / 100))
num3 = (int(resto_num2 / 10))
num4 = (int(resto_num3 / 1))

if(((num1*10 + num2)**2 + (num3*10 + num4)**2) == num)
	print(num, "atende a propriedade")
else:((num1*10 + num2)**2 + (num3*10 + num4)**2)