from numpy import *
entrando = array(eval(input("Digite o vetor: ")))
saindo = array(eval(input("Digite o vetor: ")))
elemento = 0
in_pessoas = 0
out_pessoas = 0
while(elemento < size(entrando)):
	in_pessoas = in_pessoas + entrando[elemento]
	out_pessoas = out_pessoas + saindo[elemento]
	elemento = elemento + 1

print(in_pessoas - out_pessoas)

