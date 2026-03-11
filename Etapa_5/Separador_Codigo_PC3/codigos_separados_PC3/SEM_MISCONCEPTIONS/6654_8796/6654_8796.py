from numpy import *

notas = array(eval(input()))
peso = array([1,3,2,5])
soma = notas * peso

media = sum(soma)/sum(peso) 

print(round(media, 2))