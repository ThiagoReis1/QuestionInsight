acai = float(input("Acai por m quadrado:"))
aresta = float(input("Comprimento da aresta:"))
import math
soluc = int((3*((math.sqrt(3*(aresta**2)))/2)*acai))
print(soluc)