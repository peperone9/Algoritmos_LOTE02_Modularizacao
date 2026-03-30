i: int
n1: int
n2: int
n1 = 0
n2 = 0
primo: int = 0
while(n1 == n2):
    n1 = int(input("primeiro: "))
    n2 = int(input("segundo: "))

i = n1 + 1

while(i < n2):
    if(i % 2 != 0 or i == 2):
        k = 1
        cont_divs= 0
        while(k < i):
            if(i % k == 0):
                cont_divs += 1
            k += 1
        if(cont_divs == 1):
            primo = i
            print(i)
    i += 1
