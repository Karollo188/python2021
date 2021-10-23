

####################

print("Zadanie 3.1")

# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
print("A)\njest poprawny")

#for i in "qwerty": if ord(i) < 100: print (i)

print("B)\nnie jest, zagniezdzone instrukcje (if) musza byc w oddzielnych liniach")

#for i in "axby": print (ord(i) if ord(i) < 100 else i)

print("C)\njest ok.")

########################

print("Zadanie 3.2")

#L = [3, 5, 4] ; L = L.sort()

print("A) L.sort to ktora nic nie zwraca, wiec przypisujemy do L nic. ")

#x, y = 1, 2, 3

print("B) do 2 zmiennych probujemy przypisac 3 wartosci")

# X = 1, 2, 3
# X[1] = 4

print("C) nie da sie zmienic wartosci tupla")

#X = [1, 2, 3] ; X[3] = 4

print("D) probujemy dostac sie do elementu ktory nie istnieje(X ma indeksy 0-2)")

#X = "abc"
#X.append("d")

print("E) nie da sie wykonac append. trzeby by bylo uzyc str(X.append(\"d\")")

#L = list(map(pow, range(8)))

print("F) pow przyjmuje 2 argumenty")

#####################3

print("Zadanie 3.3")

for i in range(31):
    if i % 3 != 0:
        print(i)


################

print("Zadanie 3.4")

x = input("Podaj liczbe / stop")
while x != "stop":
    try:
        print(pow(float(x),3))
    except ValueError:
        print("Zle dane")
    x = input("Podaj liczbe / stop")

################

print("Zadanie 3.5")
n = 30
print("|",end='')
for i in range(n):
    print("...0|", end='')
print("\n0",end='')
for i in range(1,n+1):
    print(f'{i:>5}', end='')

###############

print("\nZadanie 3.6")
a, b = 4, 3
for i in range(a):
    print("\n+", end='')
    for j in range(b):
        print("---+", end='')
    print('\n|',end='')
    for j in range(b):
        print("   |", end='')
print('\n+',end='')
for j in range(b):
    print("---+", end='')

#################

print("\nZadanie 3.7")
class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".fomat(self.s)

# time1 = Time(12)
# time2 = Time(3456)
#print(time1, time2)            # Python wywołuje str(), Python 2
#print [time1, time2]          # Python wywołuje repr(), Python 2

######################

print("Zadanie 3.8")
s1 = ['cat', 'dog', 'elephant', 'bee', 'human']
s2 = ['rhino', 'bee', 'monkey', 'cat', 'ant']
print(list(set(s1).intersection(s2)))
print(list(set(s1).symmetric_difference(s2)))

####################

print("Zadanie 3.9")
s1 = [[],[4],(1,2),[3,4],(5,6,7)]
for s in s1:
    print(sum(s),end=' ')

##################

print("\nZadanie 3.10")

def roman2int(number):
    prev = 0
    normal_value = 0
    for letter in number:
        if letter == 'I':
            value = 1
        elif letter == 'V':
            value = 5
        elif letter == 'X':
            value = 10
        elif letter == 'L':
            value = 50
        elif letter == 'C':
            value = 100
        elif letter == 'D':
            value = 500
        elif letter == 'M':
            value = 1000

        if value > prev:
            normal_value -= prev
        else:
            normal_value += prev

        prev = value

    normal_value += prev
    return normal_value

print(roman2int("XMIII"))
print(roman2int("DIX"))
print(roman2int("LMDCCI"))