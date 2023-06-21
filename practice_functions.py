def find_square_root(x):
    for i in range(x // 2):
        if i * i == x:
            return i
    return -1


def product_by_addition(a, b):
    if a == 0:
        return 0

    return b + product_by_addition(a - 1, b)


# sorry andrew ik this is not the fastest
# but proving a sieve is hard T_T
def is_prime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
