vet=input("string: ")
vo=0
con=0
for i in range(len(vet)):
	if vet[i]=="a" or vet[i]=="e" or vet[i]=="i" or vet[i]=="o" or vet[i]=="u":
		vo=vo+1
	else:
		con=con+1
print(vo)
print(con)