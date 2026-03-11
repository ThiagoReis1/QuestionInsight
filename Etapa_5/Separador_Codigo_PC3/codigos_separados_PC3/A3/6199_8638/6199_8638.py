alturac = 1.8
taxac= 0.01

anos = 0

alturap = float(input("altura: "))
taxap = float(input("taxa: "))

while alturap > alturac:
	altura = alturap * taxap - alturac * taxac
print(altura)