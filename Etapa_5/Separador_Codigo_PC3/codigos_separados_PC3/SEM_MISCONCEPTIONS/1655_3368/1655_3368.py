from numpy import *
from numpy.linalg import *

notas = array(eval(input("M:")))
soma=sum(notas)        
q=size(notas)    
print(round(soma/q,2))  
