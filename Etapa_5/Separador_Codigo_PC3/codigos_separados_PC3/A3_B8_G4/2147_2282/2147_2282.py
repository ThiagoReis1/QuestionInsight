s = input("")

a=0
b=0

for i in range(len(s)):
	if s[i].islower() == True:
		a = 1
	elif s[i].isupper() == True:
		b = 1
if a ==1 and b ==1 and len(s) >=11:
	print("SENHA VALIDA")
else:
	print("INVALIDO")