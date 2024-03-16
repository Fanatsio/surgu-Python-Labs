def skip_add(n, sum = 0):
    """ Принимает число n и возвращает сумму n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Использование циклов запрещено!
    >>> from construct_check import check
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    if (n > 0):
        sum += n
        return skip_add(n - 2, sum)
    else:
        return sum

def summation(n, term):

    """Возвращает сумму первых n элементов в поледовательности, заданной term.
    Реализовать с помощью рекурсии!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Использование циклов запрещено!
    >>> from construct_check import check
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
        return summation(n-1, term) + term(n)
    

def paths(m, n):
    """Возвращает число путей из нижнего левого угла сетки M x N с координатами (0, 0)
    в верхний правый (M-1, N-1), используя только сдвиги вправо или вверх.

        finish
          v
    ---------
    | > | o |
    ---------
    | * | ^ |
    ---------
      ^
    start

    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m <= 0 or n <= 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)



def max_subseq(n, t):
    """
    Возвращает максимальную по значению подпоследовательность длины в интервале [1, t],
    которую можно составить из цифр числа n, следуя по слева направо, но не обязательно подряд.
    Например, для n = 20125 и t = 3, такими подпоследовательностями будут:
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    из них наибольшим будет число 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # учтите, что 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # нулевая длина
    0
    >>> max_subseq(12345, 1)
    5
    """
    if not n or not t:
        return 0
    first = max_subseq(n // 10, t - 1) * 10 + n % 10
    second = max_subseq(n // 10, t)
    return first if first > second else second
