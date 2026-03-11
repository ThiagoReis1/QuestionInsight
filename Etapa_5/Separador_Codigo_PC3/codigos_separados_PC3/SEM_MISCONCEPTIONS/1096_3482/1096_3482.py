num = float(input("insira um numero "))
num1= num//1000
resto_num1= num%1000
num2= resto_num1//100
resto_num2= resto_num1%100
num3=resto_num2//1
total= ((num1**3) + (num2**3)) + (num3**3))
if total==num:
	print("atende", num)
else: 
	print("nao atende",num)
	