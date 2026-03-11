from numpy import *
string = input("Digite uma palavra e descubra quantos B tem: ").upper()

i = 0 
b = 0

while i < len(string):
   if (string[i] == "B"):
      b += 1
   i += 1

print(b)