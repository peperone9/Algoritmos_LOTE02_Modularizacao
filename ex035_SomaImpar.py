#35. Receba 2 números inteiros, verifique qual o maior 
# entre eles. Calcule e mostre o resultado da somatória 
# dos números ímpares entre esses valores.


#declarar
s: int = 0 #somatoria impares
n1: int
n2: int
i: int

#inicio
s = 0

n1 = int(input())
n2 = int(input())

if(n1 > n2):
	i = n2
	#somatoria impares
	while(i <= n1):
		#valida impar
		if(i % 2 != 0):
			s += i
		i += 1
else:
	i = n1
	#somatoria impares
	while(i <= n2):
		#valida impares
		if(i % 2 != 0):
			s += i
		i += 1

print("Somatoria impares: ", s)
#fim
