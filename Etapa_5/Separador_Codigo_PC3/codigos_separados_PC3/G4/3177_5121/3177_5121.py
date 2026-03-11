from numpy import*
palavra = input("Informe uma palavra qualquer: ")
a = 0
e = 0
i = 0
o = 0
u = 0
for b in palavra:
	if(b == "a"):
		a = a + 1
	if(b == "e"):
		e = e + 1
	if(b == "i"):
		i = i + 1
	if(b == "o"):
		o = o + 1
	if(b == "u"):
		u = u + 1
print("a: ",a)
print("e: ",e)
print("i: ",i)
print("o: ",o)
print("u: ",u)