num1= int(input("Digite o numero: "))
num2= num1//1000
num3= num1 % 1000 
difnum= ((num2 - num3)** 4)
if (num1 == difnum):
	print(num1,"atende a propriedade")
else:
	print(difnum)