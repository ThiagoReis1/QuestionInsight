num=int(input())

a= num//10
resA= num%10
b= a//10
resB= a%10
c= b//10
resC= b%10

soma_dos_cubos= (resA**3) + (resB**3) + (resC**3)
print(num) 

if (soma_dos_cubos == num):
	print("atende")
else:
	print("nao atende")
