n   = int(input("insira um numero: "))
s   = 0


while(n!=0):
	s = s + n
	n = int(input("insira um numero: "))
	
if(s>0):
		m = "Direita"
elif(s<0):
		m = "Esquerda"
elif(s==0):
		m = "Inicial"
print(s)
print(m)
	
