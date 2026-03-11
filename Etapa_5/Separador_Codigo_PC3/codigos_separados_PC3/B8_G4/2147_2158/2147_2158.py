n = input("CPF: ")
c = ""

if(len(n) != 11):
	print("INVALIDO")
elif(len(n) == 11):
	c = c + n[1] + n[3] + n[5] + n[7] + n[9]
print(c)