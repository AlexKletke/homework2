# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

n = int(input('enter the number of coins: '))
import random
list = [random.randint(0, 1) for i in range(n)]
print(*list)
count = 0
for y in list:
    if list[y] == 1:
        count = count + 1
if count <= n/2:
    print(f'the minimum number of coins to flip: {count}')
else:
    print(f'the minimum number of coins to flip: {n-count}')
