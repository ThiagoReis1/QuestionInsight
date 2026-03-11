voo= int(input("tempo"))
print(round(valor, 2))
if(tempo <= 200):
	print(5000 + (100/tempo))
else:
	print(8000 + (200/tempo) + (90/tempo))