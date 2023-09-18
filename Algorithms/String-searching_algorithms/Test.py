from Naive import naive
from Rabin_Karp import r_k
from Boyer_Moore import b_m
from Knuth_Morris_Pratt import k_m_p

# The given code uses substring search algorithms to count
# the number of two-digit numbers in a string that is composed of
# the first five hundred prime numbers.

# Данный код использует алгоритмы поиска подстрок чтобы
# посчитать количество двухзначных чисел в строке состоящей
# из первых пятиста простых чисел

numbers = ''
k = 0
n = 1
while k < 500:
    prime = True
    n += 1
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        numbers = numbers + str(n)
        k += 1
two_digits = [0] * (100)
for two_digit_num in range(10, 100):
    template = str(two_digit_num)
    two_digits[two_digit_num] = naive(str(two_digit_num), numbers)
print('Наивный алгоритм: ')
print(max(two_digits))
for two_digit_num in range(10, 100):
    template = str(two_digit_num)
    # Rabin-Karp
    # Рабина-Карпа
    two_digits[two_digit_num] = r_k(str(two_digit_num), numbers)
print('Алгоритм Рабина-Карпа: ')
print(max(two_digits))
for two_digit_num in range(10, 100):
    template = str(two_digit_num)
    # Boyer-Moore
    # Бойера-Мура
    two_digits[two_digit_num] = b_m(str(two_digit_num), numbers)
print('Алгоритм Бойера-Мура: ')
print(max(two_digits))
for two_digit_num in range(10, 100):
    template = str(two_digit_num)
    # Knuth_Morris_Pratt
    # Кнута-Морриса-Пратта
    two_digits[two_digit_num] = k_m_p(str(two_digit_num), numbers)
print('Алгоритм Кнута-Морриса-Пратта: ')
print(max(two_digits))