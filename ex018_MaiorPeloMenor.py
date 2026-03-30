#declarar
n1: int
n2: int

def calculo_maior():
	if(n1 > n2):
		print(n1, "-", n2, "=", n1 - n2)
	else:
		print(n2, "-", n1, "=",n2 - n1)
	#fim
def main():
	#inicio
	global n1
	global n2
	n1 = int(input())
	n2 = int(input())
	calculo_maior()
main()
