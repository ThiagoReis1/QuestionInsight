from numpy import *

e = array(eval(input("Tipo de espada: ")))
n = array(eval(input("Danos: ")))
v = array(["CENOURA, FERRO, DWARVEN, ELVEN, DAEDRIC"])

i=0

while i < size(e) and i<size(n):
	if e[i]