A = [1, 5, 3, 4, 2,4,4]

def Quicksort(A):
    if len(A) <= 1:
        return A
    reference = A[len(A) // 2]
    small = [number for number in A if number < reference]
    equal = [number for number in A if number == reference]
    big = [number for number in A if number > reference]
    return Quicksort(big) + equal + Quicksort(small)

B = Quicksort(A)
print(B)
