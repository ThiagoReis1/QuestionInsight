from numpy import*

notas= eval(input("digite o vetor de notas: "))
				
peso =array([5, 4, 3, 2])
				
mediapond= sum(notas*peso)/ sum(peso)

print(round(mediapond, 2))