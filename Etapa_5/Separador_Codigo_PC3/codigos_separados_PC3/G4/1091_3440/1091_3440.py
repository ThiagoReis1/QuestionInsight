num = int(input("Digite um numero: "))

a = num//100
b = num%100

c = (a+b)**2
print(num)

if(c == num):
	print("atende")
else:
	print("nao atende")