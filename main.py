from typing import List


def generator(limit: int, divisor: int) -> List[int]:
    if divisor > limit:
        return []
    lst, m = [], divisor
    while m <= limit:
        lst.append(m)
        m += divisor
    return lst


def f(n: int) -> List[List[int]]:
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        return f(n-1) + [[i+1 for i in range(n)]]


if __name__ == '__main__':
    print(generator(102029, 3))
    
