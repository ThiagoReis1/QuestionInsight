from numpy import *
from math import *

# Entries

values = array(eval(input("Insert measured values: ")))

# Definitions

i = 0
n = size(values)
son = 0

# Processing

while(i < n):
	son = son + sqrt(values[i])
	i = i + 1
	
QuadAvarage = (son/n)**(2)
qa = round(QuadAvarage,2)
print(qa)

