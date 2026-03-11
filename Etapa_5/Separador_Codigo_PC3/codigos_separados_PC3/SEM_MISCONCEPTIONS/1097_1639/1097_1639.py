num=int(input("digite aqui um numero inteiro de 6 digitos:"))

num1= num//100000
resto1=num%100000

num2=resto1//10000
resto2=resto1%10000

num3=resto2//1000
resto3=resto2%1000

num4=resto3//100
resto4=resto3%100

num5=resto4//10
resto5=resto4%10

num6=resto5//1

var=((num1*100+num2*10+num3)-(num4*100+num5*10+num6))**2

if(var==num):
	print(num," atende a propriedade")
	
else:
	print(var)
	