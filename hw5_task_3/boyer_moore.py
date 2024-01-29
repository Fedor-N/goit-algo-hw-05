def boyer_moore_search(text, pattern):
    # Реалізація алгоритму Боєра-Мура
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    if m > n:
        return -1

    last_occurrence = {pattern[i]: i for i in range(m)}
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i += m - min(j, 1 + last_occurrence.get(text[i], -1))
            j = m - 1

    return -1
