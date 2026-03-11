from numpy import*
a=input("Insira a palavra criptografada: ")
b=('')
s=1
while s<(len(a)+1):
	b=b+a[-s]
	s+=1

print(b)