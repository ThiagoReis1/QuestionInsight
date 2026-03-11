idade = int(input("Informe a idade: "))
acm = 0
while(idade!=-1):
	if(idade<18):
		acm = acm + 1
	idade  = int(input("informe : "))
print(acm)