from numpy import *
import numpy as np
n = array(eval(input("senha: ")))
i = 0
vq = zeros(size(n), dtype = int)

for i in range(size(n)):
	vq[i]=n[i]*n[i]
print(vq)

