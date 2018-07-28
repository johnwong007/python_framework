#!/usr/bin/python


def permutation(items, n):
    if (n > len(items)) or (n <= 0) or (len(items) == 0):
        return
    if n == 1:
        for i in range(len(items)):
            yield [items[i]]
    else:
        for i in items:
            st = list(items)
            st.remove(i)
            for j in permutation(st, n-1):
                yield [i] + j


def combination(items, n):
    if (n > len(items)) or (n <= 0) or (len(items) == 0):
        return
    if n == 1:
        for i in items:
            yield [i]
    else:
        for i in range(len(items)):
            for j in combination(items[i+1:], n-1):
                yield [items[i]] + j

