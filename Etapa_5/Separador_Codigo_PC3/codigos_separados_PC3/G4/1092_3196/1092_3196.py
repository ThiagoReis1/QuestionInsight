num = int(input('digite o numero'))
num1 = num//100
num2 = (num%100)//10
num3 = (num%100)%10

numf = (num1**3) + (num2**3) + (num3**3)
print(num)
if num == numf:
	print('atende')
else:
	print('nao atende')