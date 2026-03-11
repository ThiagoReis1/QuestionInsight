from numpy import*
from numpy.linalg import*

jogo = array(eval(input("lets play a game: ")))
b = shape(jogo)[1]
print(b)
saida = zeros(10,dtype=int)
#a = array([1,1,1,1,1,6,7,8,9,10])
#for j in range(shape(jogo)[0]):
for jogo in range(0,b,3):
	print(jogo)