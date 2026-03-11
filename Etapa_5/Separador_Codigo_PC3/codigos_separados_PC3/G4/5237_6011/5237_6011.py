a = int(input("numero a:"))
b = int(input("numero b:"))
c = int(input("numero c:"))

if (a%2==0 and b%2==0) or (c%2==0 and a%2==0) or (b%2==0 and c%2==0):
	resultado = ("SIM")
else:
	resultado = ("NAO")
	
print(resultado)