import random
import matplotlib.pyplot as plt

###########################

def just_random(amount):
    list = [i for i in range(amount)]
    return random.sample(list,amount)

def random_nearly_sorted(amount):
    list = [i for i in range(amount)]
    for i in range(amount):
        if random.randint(0, 5) > 2:
            a = random.randint(i - 5, i + 5)
            if a >= 0 and a < 50:
                list[i], list[a] = list[a], list[i]
    return list

def random_nearly_sorted_reversed(amount):
    list = [49 - i for i in range(amount)]
    for i in range(amount):
        if random.randint(0, 5) > 2:
            a = random.randint(i - 5, i + 5)
            if a >= 0 and a < 50:
                list[i], list[a] = list[a], list[i]
    return list

def random_gauss(amount):
    list = []
    for i in range(amount):
        list.append(random.gauss(25,5))
    return list

def random_repeatable(amount, size):
    list = [0] * amount
    for i in range(amount):
        list[i] = random.randint(0, size - 1)
    return list


#######################

arr = just_random(50)
print("(a) różne liczby int od 0 do n-1 w kolejności losowej:")
print(arr)

plt.plot(arr, 'o')
plt.title("losowa kolejnosc")
plt.show()

######################

arr = random_nearly_sorted(50)
print("(b) różne liczby int od 0 do n-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji):")
print(arr)

plt.plot(arr, 'o')
plt.title("losowe, blisko dobrej pozycji")
plt.show()

######################

arr = random_nearly_sorted_reversed(50)
print("(c) różne liczby int od 0 do n-1 prawie posortowane w odwrotnej kolejności:")
print(arr)

plt.plot(arr, 'o')
plt.title("w odwroconej kolejnosci")
plt.show()

###################

arr = random_gauss(1000)
print("(d) n liczb float w kolejności losowej o rozkładzie gaussowskim:")
print(arr)

plt.hist(arr, bins=50)
plt.title("gauss")
plt.show()

#################################

arr_repeatable = random_repeatable(1000,50)
print("(e) n liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < n, np. k^2 = n):")
print(arr_repeatable)

plt.hist(arr_repeatable, bins=50)
plt.title("powtarzajace sie rys 1")
plt.show()

plt.plot(arr_repeatable, 'o')
plt.title("powtarzajace sie rys 2")
plt.show()

#############################  SORTOWANIE  #######################################

def insert_sort(arr, list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        list.append([i for i in arr])

# do list dopisuje kolejne wartosci z sortowanej tablicy

random_arr = just_random(50)
print("Tablica do posortowania:")
print(random_arr)
arr = []
print("Kolejne etapy sortowania:")
insert_sort(random_arr, arr)
print(arr)

y_values = [i for i in range(50)]

for i in range(49):
    plt.xlim(0, 49)
    plt.ylim(0, 49)
    plt.cla()
    plt.scatter(arr[i], y_values, color='black')
    plt.title("insert sort")
    plt.pause(0.01)


plt.show()