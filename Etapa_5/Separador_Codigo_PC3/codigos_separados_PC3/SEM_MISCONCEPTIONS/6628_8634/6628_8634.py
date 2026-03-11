# faça seu código aqui!
from numpy import *
palavra = input("Palavra: ").upper()
es = 0
i = 0

while i < len(palavra):
	if palavra[i] == "E":
		es +=1
	i+=1
print(es)