x = 4

if x == 4:
    print('x é = a 4')

confirma = True

if confirma:
    print("confirma é verdadeiro")
else:
    print("confirma é falso")

arr = {1,2,3,4,5,6,7,8,9}

for num in arr:
    print(num)

def caixaDeSoma(n1, n2):
    return n1 + n2

    
def caixaDeSubtração(n1, n2):
    return n1 - n2

assert caixaDeSoma(1, 5) == 6
#assert caixaDeSoma(1, 5) == 7

def caixaMagica(n1,n2):
    y =  caixaDeSubtração(n1,n2)
    if y >= 0:
        print(y)
    else:
        print(0)

caixaMagica(4,1)