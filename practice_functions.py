def find_square_root(x):
    i = 0
    while i <= x // 2:
        if i * i == x:
            return i
        i += 1
    return -1


def is_prime(x):
    if 2 >= x > 0:
        return True

    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


def product_by_addition(a, b):
    if a == 0:
        return 0

    return b + product_by_addition(a - 1, b)


# sorry andrew ik this is not the fastest
# but proving a sieve is hard T_T


def rev_bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

    return A


print(find_square_root(10))
print(find_square_root(9))

print(is_prime(1))
print(is_prime(2))
print(is_prime(7))
print(is_prime(12))
print(is_prime(15))

print(product_by_addition(0, 20))
print(product_by_addition(10, 20))

print(rev_bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
