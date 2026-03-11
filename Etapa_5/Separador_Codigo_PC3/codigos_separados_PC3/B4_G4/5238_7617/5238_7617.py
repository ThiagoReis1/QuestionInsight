num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
num3 = int(input('Digite o terceiro numero inteiro: '))

if (num1 >= 1000 and num2 >= 1000):
	print('SIM')
elif (num1 >= 1000 and num3 >= 1000):
	print('SIM')
elif (num2 >= 1000 and num3 >= 1000):
	print('SIM')
else:
	print('NAO')