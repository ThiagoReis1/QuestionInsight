from numpy import*
string= input("Digite uma string: ")
v= 0
c= 0
for i in range(len(string)):
	if(string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u"):
		v= v + 1
	else:
		c= c + 1
print(v)
print(c)