num = int(input("Escreva o numero:"))

d1 = num//1000
d2 = num%1000
c = (d1-d2)**2
if(c == num):
	print("atende")
	print(int(num))
else:
	print("nao atende")
	print(int(num))
