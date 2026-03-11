from numpy import*

ceb = input("Insira as palavras do cebolinha:\n")
normal = input("Insira uma palavra normal:\n")

i = 0
a = 0
j = 0

while(i < size(normal)):
	if(normal[i] == "r" or normal[i] == "R"):
		normal.replace("r","L")
		normal.replace("R", "L")
	i = i + 1

if(normal 