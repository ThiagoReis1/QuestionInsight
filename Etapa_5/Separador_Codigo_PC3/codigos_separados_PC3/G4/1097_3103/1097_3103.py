n = int(input("Qual o numero?: "))
N1 = (n // 1000)
N2 = (n % 1000) 
C = ( N1 - N2) ** 2
if(C == n):
	msg = "atende"
else:	
   msg = "nao atende"
print(msg)
print(n)