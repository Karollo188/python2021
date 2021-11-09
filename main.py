import cmath

print("Zadanie 4.1")
X = "qwerty"
def func():
    print ( X )
func()

print("A) wynik: qwerty. jezeli zmienna nie jest lokalna, program szuka wartosci globalnej")


X = "qwerty"

def func():
    X = "abc"

func()
print ( X )

print("B) wynik:qwerty. zmienna w funkcji jest lokalna, operujmy na kopiach")

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print ( X )

print("C) wynik: abc. funkcja tworzy zmienna globalna, dlatego nadpisuje poprzednia wartosc")

#############################

print("Zadanie 4.2")

def trzy_pienc(n):
    print("|",end='')
    b = ""
    for i in range(n):
        b = b+ "....|"
    b = b + "\n0"
    for i in range(1,n+1):
        b = b + '{0:>5}'.format(i)
    return b

print(trzy_pienc(20))
###############
def trzy_szesc(a,b):
    r = ""
    for i in range(a):
        r = r + "\n+"
        for j in range(b):
            r = r + "---+"
        r = r + '\n|'
        for j in range(b):
            r = r + "   |"
    r = r + '\n+'
    for j in range(b):
        r = r + "---+"
    return r

print(trzy_szesc(3,4))

##################3

print("Zadanie 4.3")

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(5))

#################

print("Zadanie 4.4")

def fibonacci(n):
    a = ((1 + pow(5,1/2))/2)
    b = ((1 - pow(5,1/2))/2)


    for i in range(n):
        a = a * a
        b = b * b

    return  ((1/pow(5,1/2)) * a) - ((1/pow(5,1/2)) * b)

print(fibonacci(4))


################

print("Zadanie 4.5")

def odwracanie(L, left, right):
    for i in range (left,int((right + left) / 2)):
        L[i], L[right - i + left] = L[right - i + left], L[i]

list = [1,2,3,4,5,6,7,8,9]
odwracanie(list,2,7)
print(list)

def odwracanie_rec(L, left, right):
    if(left < right):
        L[left], L[right] = L[right], L[left]
        odwracanie_rec(L, left+1, right-1)

odwracanie_rec(list,2,7)
print(list)

#######################

print("Zadanie 4.6")

def sum_seq(sequence):
    res = [elem for elem in sequence if elem != []]
    sum = 0
    for s in res:
        if(isinstance(s,int)):
            sum = sum + s
        else:
            sum = sum + sum_seq(s)
    return sum

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print(sum_seq(seq))

########################

print("Zadanie 4.7")

def flatten(sequence):
    res = [elem for elem in sequence if elem != []]
    flat = []
    for s in res:
        if(isinstance(s,int)):
            flat.append(s)
        else:
            flat.append(item for sublist in s for item in sublist)


    return list

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

print ( flatten(seq) )   # [1,2,3,4,5,6,7,8,9]