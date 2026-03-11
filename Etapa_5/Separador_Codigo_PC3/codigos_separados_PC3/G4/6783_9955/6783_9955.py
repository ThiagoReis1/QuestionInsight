ano=int(input())
pais=input().upper()
idade=2023-ano

if (pais=="B")and(idade>=18):
	print("sim")
	h=idade-18
	print(h)
elif (pais=="B")and(idade<18):
	print("nao")
	h=18-idade
	print(h)
elif (pais=="E")and(idade>=16):
	print("sim")
	h=idade-16
	print(h)
elif (pais=="E")and(idade<16):
	print("nao")
	h=16-idade
	print(h)
else:
	print("invalido")
