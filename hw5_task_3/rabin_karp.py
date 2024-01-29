def rabin_karp_search(text, pattern):
    # Реалізація алгоритму Рабіна-Карпа
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    if m > n:
        return -1

    prime = 101  # можна обрати будь-яке просте число

    def hash_function(s):
        return sum(ord(s[i]) * pow(prime, i) for i in range(len(s)))

    pattern_hash = hash_function(pattern)
    text_hash = hash_function(text[:m])

    for i in range(n - m + 1):
        if pattern_hash == text_hash and pattern == text[i:i + m]:
            return i
        if i < n - m:
            text_hash = (text_hash - ord(text[i])) / \
                prime + ord(text[i + m]) * pow(prime, m - 1)

    return -1
