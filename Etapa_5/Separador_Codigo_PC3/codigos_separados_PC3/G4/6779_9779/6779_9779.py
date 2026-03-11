ano=int(input("nasc:"))
pais=input("pais:").upper()

idade=2023-ano

if (pais=="B")and(idade>=18):
	print("sim")
	f=idade-18
	print(f)
	
elif (pais=="B")and(idade<18):
	print("nao")
	f=18-idade
	print(f)
	
elif (pais=="J")and(idade>=16):
	print("sim")
	f=idade-16
	print(f)
	
elif (pais=="J")and(idade<16):
	print("nao")
	f=16-idade
	print(f)
	
else:
	print("invalido")