l= int(input("qual o resultado do lancamento:"))

i=0
t= 0

while(l!=-1):
	t= t + 1
	if(l==5):
		i= i + 1
	l= int (input("qual o resultado do lancamento:"))
	
print(t)
print(round((i*100)/t,2))