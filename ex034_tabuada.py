#34. Receba um número. Calcule e mostre os resultados da tabuada
# desse número.

#declarar
i: int
n: int




def tabuada():
	global n 
	#inicio
	i = 0
	n = int(input("Numero da tabuada: "))
	while(i <= 10):
		print(n,"x",i,"=",n*i)
		i += 1
#fim
def main():
	tabuada()
main()

