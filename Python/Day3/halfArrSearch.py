"""
Binarna pretraga - za dati niz celih brojeva, vratiti indeks trazenog broja.
Ukoliko broj nije pronadjen, vratiti -1.

Vremenska kompleksnost: O(log n)

Pseudocode:
procedure binarnaPretraga(lista : lista celih brojeva, trazeniBroj : ceo broj):
    start = 0
    end = duzina(lista) - 1
    srednjiIndeks = 0

    while start <= end:
        srednjiIndeks = (start + end) // 2
        if lista[srednjiIndeks] < trazeniBroj:
            # broj koji trazimo je u desnoj polovini
            granica za start = srednjiIndeks + 1
        else if lista[srednjiIndeks] > trazeniBroj:
            # broj koji trazimo je u levoj polovini
            granica za end = srednjiIndeks - 1
        else:
            pronasli smo broj na srednjiIndeks
            return srednjiIndeks
    end while
    return -1
end procedure

"""
def binarnaPretraga(lista, trazeniBroj):
    start = 0
    end = len(lista) - 1
    srednjiIndeks = 0

    while start <= end:
        srednjiIndeks = (start + end) // 2
        if lista[srednjiIndeks] < trazeniBroj:
            start = srednjiIndeks + 1
        elif lista[srednjiIndeks] > trazeniBroj:
            end = srednjiIndeks - 1
        else:
            return srednjiIndeks
    return -1

