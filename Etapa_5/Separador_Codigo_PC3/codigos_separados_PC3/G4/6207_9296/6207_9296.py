n = int(input("Qual o valor digitado? "))
cont = 0
while(n != -1):
	if( n >= 26 and n <= 50):
		cont = cont + 1
	n = int(input("qual 0 valor digitado? "))
		
print(cont)