import timeit
from boyer_moore import boyer_moore_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search


def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


if __name__ == "__main__":
    with open("Article_1.txt", "r", encoding="utf-8") as file:
        article1_text = file.read()

    with open("Article_2.txt", "r", encoding="utf-8") as file:
        article2_text = file.read()

    existing_pattern_A_1 = "При знаходженні елемента повертається його позиція у структурі даних"
    fictional_pattern_A_1 = "Рекомендаційні системи є важливою складовою"

    existing_pattern_A_2 = "Рекомендаційні системи є важливою складовою"
    fictional_pattern_A_2 = "При знаходженні елемента повертається його позиція у структурі даних"

    # Виміряти час виконання для кожного алгоритму і підрядка для статті 1
    bm_existing_time_article1 = measure_time(
        boyer_moore_search, article1_text, existing_pattern_A_1)
    kmp_existing_time_article1 = measure_time(
        kmp_search, article1_text, existing_pattern_A_1)
    rk_existing_time_article1 = measure_time(
        rabin_karp_search, article1_text, existing_pattern_A_1)

    bm_fictional_time_article1 = measure_time(
        boyer_moore_search, article1_text, fictional_pattern_A_1)
    kmp_fictional_time_article1 = measure_time(
        kmp_search, article1_text, fictional_pattern_A_1)
    rk_fictional_time_article1 = measure_time(
        rabin_karp_search, article1_text, fictional_pattern_A_1)

    # Вивести результати для статті 1
    print("Article 1 Results:")
    print("Boyer-Moore Existing Time:", bm_existing_time_article1)
    print("KMP Existing Time:", kmp_existing_time_article1)
    print("Rabin-Karp Existing Time:", rk_existing_time_article1)
    print("Boyer-Moore Fictional Time:", bm_fictional_time_article1)
    print("KMP Fictional Time:", kmp_fictional_time_article1)
    print("Rabin-Karp Fictional Time:", rk_fictional_time_article1)

    # Виміряти час виконання для кожного алгоритму і підрядка для статті 2
    bm_existing_time_article2 = measure_time(
        boyer_moore_search, article2_text, existing_pattern_A_2)
    kmp_existing_time_article2 = measure_time(
        kmp_search, article2_text, existing_pattern_A_2)
    rk_existing_time_article2 = measure_time(
        rabin_karp_search, article2_text, existing_pattern_A_2)

    bm_fictional_time_article2 = measure_time(
        boyer_moore_search, article2_text, fictional_pattern_A_2)
    kmp_fictional_time_article2 = measure_time(
        kmp_search, article2_text, fictional_pattern_A_2)
    rk_fictional_time_article2 = measure_time(
        rabin_karp_search, article2_text, fictional_pattern_A_2)

    # Вивести результати для статті 2
    print("\nArticle 2 Results:")
    print("Boyer-Moore Existing Time:", bm_existing_time_article2)
    print("KMP Existing Time:", kmp_existing_time_article2)
    print("Rabin-Karp Existing Time:", rk_existing_time_article2)
    print("Boyer-Moore Fictional Time:", bm_fictional_time_article2)
    print("KMP Fictional Time:", kmp_fictional_time_article2)
    print("Rabin-Karp Fictional Time:", rk_fictional_time_article2)

    # Загальні результати
    total_bm_existing_time = bm_existing_time_article1 + bm_existing_time_article2
    total_kmp_existing_time = kmp_existing_time_article1 + kmp_existing_time_article2
    total_rk_existing_time = rk_existing_time_article1 + rk_existing_time_article2

    total_bm_fictional_time = bm_fictional_time_article1 + bm_fictional_time_article2
    total_kmp_fictional_time = kmp_fictional_time_article1 + kmp_fictional_time_article2
    total_rk_fictional_time = rk_fictional_time_article1 + rk_fictional_time_article2

    print("\nTotal Results:")
    print("Total Boyer-Moore Existing Time:", total_bm_existing_time)
    print("Total KMP Existing Time:", total_kmp_existing_time)
    print("Total Rabin-Karp Existing Time:", total_rk_existing_time)
    print("Total Boyer-Moore Fictional Time:", total_bm_fictional_time)
    print("Total KMP Fictional Time:", total_kmp_fictional_time)
    print("Total Rabin-Karp Fictional Time:", total_rk_fictional_time)
