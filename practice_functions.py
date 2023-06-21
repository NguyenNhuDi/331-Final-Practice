def find_square_root(x):
    for i in range(x // 2):
        if i * i == x:
            return i
    return -1


