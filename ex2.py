# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
N = int(input('enter number from 1 to 10000: '))
summa = 0
for i in range(0, N+1):
    summa = summa + i
print(f'the sum of integers located between the numbers 1 and N = {summa}')
