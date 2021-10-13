line = ("fsdfd\nfdsfdsfds fsfs\nersfs fsfdsf fs\n  xsdfs")
tmpline = ""

######################

print("Zadanie 2.10: ")
print(str(len(line.split())))

#####################

print("Zadanie 2.11")
for letter in line:
    tmpline += (letter + "_")
print(tmpline)
tmpline = ""

####################

print("Zadanie 2.12")
print("Z pierwszych znakow: ")
for word in line.split():
    print(word[0], end = '')
print("\nZ ostatnich znakow: ")
for word in line.split():
    print(word[-1], end = '')

####################

sum = 0
print("\nZadanie 2.13")
for word in line.split():
    sum += len(word)
print(sum)

###################

length = 0
longest = ""
print("Zadanie 2.14")
for word in line.split():
    if len(word) > length:
        length = len(word)
        longest = word

print("wyraz: " + longest + " dlugosc: " + str(length))

###################

line = ""
print("Zadanie 2.15")
L = (113,234,543,234,876,45)
for value in L:
    line += str(value)
print(line)

##################

line = "dsafsdGvRfdsf GvR daf"
print("Zadanie 2.16")
print(line.replace("GvR", "Guido van Rossum"))

###################

line = "i have a grey cat"
print("Zadanie 2.17\nAlfabetycznie: ")
tmpline = line.split()
tmpline.sort()
for word in tmpline:
    print(word + " ", end='')
print("\nPo dlugosci:")
tmpline = line.split()
tmpline.sort(key = len, reverse=True)
for word in tmpline:
    print(word + " ", end='')

####################

print("\nZadanie 2.18")
a = 12301204020340204020
print (str(a).count("0"))

####################

print("Zadanie 2.19")
L = (122,543,123,876,424,43,12,7,3,312,3)
line = ""
for value in L:
    print(str(value).zfill(3), end='')

#([x*x for x in range(100)]) #- generator