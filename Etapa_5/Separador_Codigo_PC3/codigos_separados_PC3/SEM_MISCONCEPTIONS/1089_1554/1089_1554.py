x= float(input())
y= float(input())
z= float(input())
lim= float(input())
total= (x + y + z)
if(total <= lim):
	mensagem= "Sim"
else:
	mensagem= "Nao"
	
print(round(total,2))
print(mensagem)