permutations = []


def generate(A, size):
    if size == 1:
        permutations.append(A[::])
        return

    for i in range(size):
        generate(A, size - 1)
        if size & 1:
            A[0], A[size-1] = A[size-1], A[0] #If Odd
        else:
            A[i], A[size-1] = A[size-1], A[i] # If Even


A = ["X", "Y", "Z"]
n = len(A)
generate(A, n)
print(permutations)
