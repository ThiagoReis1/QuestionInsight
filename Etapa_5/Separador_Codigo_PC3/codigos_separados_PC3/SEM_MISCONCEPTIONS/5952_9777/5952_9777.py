t = 3.50
s = 5.00
a = 13.00

comida=input("S/T:")
quant=int(input("quant:"))
quantr=int(input("quant:"))

qacai=quantr*a
if comida=="S":
	val=s*quant+qacai
else:
	val=t*quant+qacai
	
print(round(val,2))
