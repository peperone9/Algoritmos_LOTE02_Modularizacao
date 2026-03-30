#31. Calcule e mostre o quadrado dos números entre 10 e 150.

#declarar
i: int
def quadrados(n, intervalo):
	i = n 
	while(i <= intervalo):
		print(i*i)
		i += 1
	print()
	#fim

def main():
	global i 
	i = 10
	quadrados(i, 150)
main()

