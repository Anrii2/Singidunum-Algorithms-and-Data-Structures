"""
Pseudo code:
procedure selectionSort(A : list of sortable items)
    n = length(A)

    for i = 0 to n:
    trazimo najmanji element u nesortiranom delu niza
        minIndex = i
        for j = i + 1 to n:
            if A[j] < A[minIndex]:
                minIndex = j
    zamenjujemo najmanji element sa prvim elementom nesortiranog dela niza
    swap(A[i], A[minIndex])
    end for

    end procedure
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


nasa_lista = [64, 25, 12, 22, 11]
print("Nesortirana lista:", nasa_lista)
selection_sort(nasa_lista)
print("Sortirana lista:", nasa_lista)