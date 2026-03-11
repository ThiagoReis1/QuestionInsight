from numpy import*
from numpy.linalg import*
m = array(eval(input('Matriz: ')))
lin = shape(m)[0]
col = shape(m)[1]
maior = 0
indice = 0
for i in range(lin):
    for j in range(col):
      if m[i][j] > maior:
            indice = i
            maior = m[i][j]
      else:
            j += 1
print(maior)    			
       
		 