soma = 0
number1 = input("digite um numero inteiro ---> ")
number2 = input("digite outro numero inteiro ---> ")
if number1 < number2:
	while number1 < number2:
		number1 = number1 + 1        
		soma = soma + number1
		if number1 < number2:
			print(number1)
 
elif number2 < number1:
	while number2 < number1:
	number2 = number2 + 1
	soma = soma + number2
		if number2 < number1:
			print(number2)