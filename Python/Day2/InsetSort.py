"""
Insert sort

pseudokod:
procedure insertionSort(arr : list of elements):
    n = length(arr)
    for i = 1 to n-1:
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        end while
        arr[j + 1] = key
    end for
end procedure

"""
import random
import time
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def measure(arr, repeats=1000):
    total_time = 0.0
    for _ in range(repeats):
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        insertion_sort(arr_copy)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return total_time / repeats


nasa_lista = [random.randint(0, 1_000_000) for _ in range(1000)]
print("Nesortirana lista:", nasa_lista)
prosecno_vreme = measure(nasa_lista, repeats=1000)
print(f"Prosecno vreme izvrsavanja InsertSorta: {prosecno_vreme:.15f} sekundi")
insertion_sort(nasa_lista)
print("Sortirana lista:", nasa_lista)
