def merge_sort(a):
    if len(a) > 1:
        m = len(a)//2
        L, R = a[:m], a[m:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]; i += 1
            else:
                a[k] = R[j]; j += 1
            k += 1
        a[k:] = L[i:] + R[j:]

a = list(map(int, input("Enter numbers: ").split()))
merge_sort(a)
print("Sorted:", a)