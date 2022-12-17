# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

N = int(input('enter number from 1 to 1000000: '))
for i in range(2, N+1):
    if N % i == 0:
        print(f'the smallest natural divisor of an integer {N}: {i}')
        exit()


