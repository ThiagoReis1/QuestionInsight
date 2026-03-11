num= int(input("Digite um numero"))
print(num)
a = num//1000
b= num%1000
calculo= (a-b)**4
if(calculo == num):
	print("atende")
else:
	print("nao atende")