from numpy import *
from numpy.linalg import *

tb = array(eval(input("Tempos dos Banhos: ")))

at = array(eval(input("Percentual de abertura de torneira: ")))
at = (at / 100) * 5
at = at.T

ct = dot( tb, at )

print(ct)