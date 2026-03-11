num = int(input("insira um numero"))
cont = 0

while num!= -1:
	if(num >= 26 and num<=50):
		cont+=1
	num = int(input("insira um numero"))

print(cont)