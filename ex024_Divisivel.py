# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

# Valores divisiveis por 2 e 3: 0 6 18
# Valores não divisiveis por 2 e 3: 4 9 15

#declarar
valor: int

def validar_divisao():
	if(valor % 2 == 0 and valor % 3 ==0):
		print(valor, "e divisivel por 2 e 3")
	else:
		print(valor, "nao eh divisivel por 2 e 3")

def main():
	#inicio
	global valor 
	valor = int(input())
	validar_divisao()
main()
