limite = float(input())
v1= float(input())
v2= float(input())
v3= float(input())
v4=float(input())

valortotal = v1+v2+v3+v4

print(round(valortotal,2))

if(valortotal<=limite):
	print("Dentro do limite")
else:
	print("Estourou o limite")