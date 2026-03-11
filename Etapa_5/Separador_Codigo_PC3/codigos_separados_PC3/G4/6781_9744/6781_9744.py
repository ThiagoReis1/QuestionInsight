nas= int(input())
p = input()
idade = 2023-nas
apto = 2023-(nas+18)
aa = 18-idade
bb = 21-idade
if((p.upper())== "B" or "E"):
	if(p.upper()=="E"):
		if(idade>=18):
			print("sim")
			print(apto)
		else:
			print("nao")
			print(aa)
	else:
		if(p.upper()=="B"):
			if(idade>=21):
				print("sim")
				print(apto)
			else:
				print("nao")
				print(bb)

		else:
			print("invalido")

	