import random

# Napisać program, który na listę L wstawi n liczb wylosowanych z zakresu od 0 do k-1.
# Następnie program wylosuje liczbę y z tego samego zakresu i znajdzie wszystkie jej wystąpienia na liście L przy pomocy wyszukiwania liniowego. [n=100, k=10]

L = []
k_arr = [0] * 10
k = 10
n = 100

for i in range(n):
    L.append(random.randint(0,k-1))

print(L)

# for i in range(n):
#     k_arr[L[i]] += 1
#
# print(k_arr)

y = random.randint(0,k-1)
print(y)

for i in range(n):
    if L[i] == y:
        print(i, end=' ')
print()

##########################################

# Napisać wersję rekurencyjną wyszukiwania binarnego.

L = [i for i in range(100)] #tablica posortoana


def bin_search_rec(arr, L, H, value):
    if H >= L:

        mid = (H + L) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return bin_search_rec(arr, L, mid - 1, value)
        else:
            return bin_search_rec(arr, mid + 1, H, value)

    else:
        return -1

print(bin_search_rec(L, 0, len(L), 0))