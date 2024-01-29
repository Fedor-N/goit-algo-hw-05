def binary_search(arr, target):
    # Ініціалізуємо змінні для ведення лічильника інтерацій та верхньої межі
    iterations = 0
    upper_bound = None

    # Встановлюємо початкові значення для пошуку
    left, right = 0, len(arr) - 1

    while left <= right:
        # Збільшуємо лічильник інтерацій
        iterations += 1

        # Знаходимо середину масиву
        mid = left + (right - left) // 2

        # Перевіряємо, чи елемент у середині масиву менший, більший або рівний цільовому значенню
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            # Оновлюємо верхню межу при знаходженні елемента, який більший або рівний цільовому значенню
            upper_bound = arr[mid]
            right = mid - 1

    # Повертаємо кортеж з кількістю інтерацій та верхньою межею
    return iterations, upper_bound


# Приклад використання:
sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
target_value = 1.0

result = binary_search(sorted_array, target_value)
print(result)
