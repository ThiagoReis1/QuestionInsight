a = int(input("digite um valor:"))
p = input("digite:").upper()

d = 2023 - a

if(p=="B") and(d>=18):
	v = d - 18
	print("sim")
	print(v)
elif(p=="B") and (d<18):
	v = 18-d
	print("nao")
	print(v)
elif(p=="I") and (d>=17):
	print("sim")
	v = d -17
	print(v)
elif(p=="I") and(d<17):
	v = 17-d
	print("nao")
	print(v)
else:
	print("invalido")