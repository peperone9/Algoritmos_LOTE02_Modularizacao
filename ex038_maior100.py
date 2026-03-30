
i:int
n: int
maior: int
menor: int

i = 0
while(i < 5):
	n = int(input())
	if(n > 0):
		if(i == 0):
			maior = n
			menor = n
		else:
			if(n > maior):
				maior = n
			if(n < menor):
				menor = n
		i += 1
	else:
		print("o numero precisa ser positivo")
print(f"maior: {maior}, menor: {menor}")
