num = int(input("digite um valor: "))
 
a = num//1000
b = num //100 % 10
c = num //10 %10
d = num % 10


cal= (a * b + c *d)**2
if(cal >= 1102):
	print(cal)
	print("atende")
else:
	print(cal)
	print("nao atende")