num= int(input("digite o numero: "))

num1= num//1000
num2= num%1000

if(num==((num1-num2)**2)):
	print("atende")
	print(num)
else: 
	print("nao atende")
	print(num)
	
