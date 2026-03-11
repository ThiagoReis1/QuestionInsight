# faça seu código aqui!
t = input("combo ").upper()
q = int(input("q. "))
v = 0

if t == "C":
	v = round((30*q)*0.85,2)
else:
	v = round(30*q,2)
	
print(v)