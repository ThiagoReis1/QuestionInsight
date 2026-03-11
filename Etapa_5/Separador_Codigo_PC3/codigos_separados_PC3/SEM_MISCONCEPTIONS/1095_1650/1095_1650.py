num = int(input("29990001"))
num1= num // 10000000
resto1= num % 10000000
num2= resto1 // 1000000
resto2 = resto1 % 1000000
num3= resto2 // 100000
resto3= resto2 % 100000
num4= resto3 // 10000
resto4= resto3 % 10000
num5= resto4 // 1000
resto5= resto4 % 1000
num6 = resto5 // 100
resto6 = resto5 % 100
num7 = resto6 // 10
resto7 = resto6 % 10
num8= resto7 // 1

var = ((num1*1000+num2*100+num3*10+num4) + (num5*1000+num6*100+num7*10+num8))**2

if (var == num):
	print("29990001 atende a propriedade")
	
else:
	print(var)