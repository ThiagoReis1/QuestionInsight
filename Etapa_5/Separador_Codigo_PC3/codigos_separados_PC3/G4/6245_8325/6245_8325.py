r=input("resposta do cliente: ")

c=0

while(r.upper()!="X"):
	if(r.upper()=="S"):
		c=c+1
	r=input("resposta do cliente: ")

print(c)