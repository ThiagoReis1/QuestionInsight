so=int(input("Posicao: "))
v=int(input("valocidade: "))
t=int(input("tempo de deslocamento: "))
s=so+v*t
print(s)
if(v<=100):
	print("OK")
else:
	print("ACIMA")