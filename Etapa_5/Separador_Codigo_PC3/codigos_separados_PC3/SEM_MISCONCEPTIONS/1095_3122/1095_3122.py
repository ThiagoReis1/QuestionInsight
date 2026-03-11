num = int(input("Num: "))

digito1 = num // 10000000
# print(digito1)
digito2 = (num // 1000000) % 10
# print(digito2)
digito3 = (num // 100000) % 10
# print(digito3)
digito4 = (num // 10000) % 10
# print(digito4)
digito5 = (num // 1000) % 10
# print(digito5)
digito6 = (num // 100) % 10
# print(digito6)
digito7 = (num // 10) % 10
# print(digito7)
digito8 = num % 10
# print(digito8)

num1 = digito1 * 1000
num2 = digito2 * 100
num3 = digito3 * 10
num4 = digito4

num5 = digito5 * 1000
num6 = digito6 * 100
num7 = digito7 * 10
num8 = digito8

bloco1 = num1 + num2 + num3 + num4
# print(bloco1)
bloco2 = num5 + num6 + num7 + num8
# print(bloco2)
soma = (bloco1+bloco2)**2
# print(soma)

if(soma == num):
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")





