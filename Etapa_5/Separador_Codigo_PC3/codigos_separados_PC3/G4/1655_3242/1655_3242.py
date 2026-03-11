from numpy import *
from numpy.linalg import *

s = input("Insira uma string: ").lower().upper()

AC = s.count('AC')
AM = s.count('AM')
PA = s.count('PA')
RO = s.count('RO')
RR = s.count('RR')


v =  AC + AM + PA + RO + RR
c = len(s) - v
print(v)
print(c)
