#n1 < n2: 1 2 | -2 -1
#n2 < n1: 2 1 | -1 -2
#iguais: 1 1

n1: int
n2: int

def ler_numeros():
	global n1 
	global n2
	n1 =  int(input("primeiro: "))
	n2 = int(input("segundo: "))

def ordena_num():
	if(n1 <  n2):
		print(n1, n2, end=" ")
	elif(n2 < n1):
		print(n2, n1, end=" ")
	else:
		print("Os valores precisam  ser diferentes")

def main():
	ler_numeros()
	ordena_num()
main()