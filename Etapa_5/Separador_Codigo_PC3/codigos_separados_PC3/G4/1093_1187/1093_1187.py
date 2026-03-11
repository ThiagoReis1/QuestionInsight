num = int(input("Numero:"))
num1 = num // 100
num2 = num % 100
s = (((num1)**2) + ((num2)**2))
if (num == s):
	print(num, "atende a propriedade")
else:
	print(s)
