num = int(input("informe o numero: "))
val = num//1000
vall = num%1000
total = (val - vall)**4

if(num == total):
	msg = "atende"
else:
	msg = "nao atende"
print(num)	
print(msg)