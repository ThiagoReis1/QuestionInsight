senha= input("digite a senha:").upper()

i=0
total=0
while(i<len(senha)):
	if (senha[i]== "A" or senha[i]=="E" or senha[i]== "I" or senha[i]=="O" or senha[i]== "U"):
		total= total + 1.12
	else:
		total= total+ 1.18
	i=i+1
	
print (round(total,2))
