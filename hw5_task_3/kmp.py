def kmp_search(text, pattern):
    # Реалізація алгоритму Кнута-Морріса-Прата
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    if m > n:
        return -1

    prefix_table = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_table[i] = j

    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = prefix_table[j - 1]
            else:
                i += 1

    return -1
