def find_square_root(x):
    for i in range(x // 2):
        if i * i == x:
            return i
    return -1


def product_by_addition(a, b):
    if a == 0:
        return 0

    return b + product_by_addition(a - 1, b)

