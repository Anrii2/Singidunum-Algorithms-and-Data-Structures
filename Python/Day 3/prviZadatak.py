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


nasa_lista = [64, 34, 25, 12, 22, 11, 90, 1432, 12983, 2131, 123123, 666523, 124674, 12983618723, 1298371, 218937, 1092, 1287365, 12387912, 5555, 123452134]
print("Nesortirana lista:", nasa_lista)
bubble_sort(nasa_lista)
print("Sortirana lista:", nasa_lista)