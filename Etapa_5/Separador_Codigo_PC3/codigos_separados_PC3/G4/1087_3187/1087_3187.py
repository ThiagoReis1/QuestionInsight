a = float(input("qual a nota"))
b = float(input("qual a nota"))
c = float(input("qual a nota"))
d = float(input("qual a nota"))
x = round(((a + b + c + d) / 4), 2)
print(x)
if(x >= 7.0):
	print("Aprovado")
else: 
	print("Reprovado")
