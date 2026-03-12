"""
Faktorijel broja n je proizvod svih pozitivnih celih brojeva od 1 do n. Na primer, faktorijel broja 5 (označava se kao 5!) je 1 * 2 * 3 * 4 * 5 = 120.
Vremenska kompleksnost: O(n)
Pseudocode:
procedure faktorijel(n : ceo broj):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorijel(n - 1)
end procedure

"""
def faktorijel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorijel(n - 1)