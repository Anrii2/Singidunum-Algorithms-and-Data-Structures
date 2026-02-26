"""
Bubble sort
Pseudokod:

procedure bubbleSort(arr : lisa elemenata):
    n = length(arr)
    for i = 0 to n-1:
        for j = 0 to n-i-2:
            hasSwapped = false
            for j = 0 to n-1-i:
                if arr[j] > arr[j+1]:
                    swap(arr[j], arr[j+1])
                    hasSwapped = true
        end for
    end for
end procedure
"""
import time
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        hasSwapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hasSwapped = True
        if not hasSwapped:  
            break
    return arr

def measure(arr, repeats=1000):
    total_time = 0.0
    for _ in range(repeats):
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        bubble_sort(arr_copy)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return total_time / repeats

nasa_lista = [random.randint(0, 1_000_000) for _ in range(1000)]
print("Nesortirana lista:", nasa_lista)
prosecno_vreme = measure(nasa_lista, repeats=1000)
print(f"Prosecno vreme izvrsavanja BubbleSorta: {prosecno_vreme:.15f} sekundi")
bubble_sort(nasa_lista)
print("Sortirana lista:", nasa_lista)