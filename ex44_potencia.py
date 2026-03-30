base: float #base
exp: int #expoent
pot: float

base = float(input())
exp = int(input())
pot = base
if(exp > 0):
	while(exp > 1):
		pot *= base
		exp -= 1
elif(exp < 0):
	while(exp <= 0):
		pot /= base
		exp += 1
else:
	pot = 1
print(pot)
