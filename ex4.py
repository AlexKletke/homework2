# Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, если заранее известен рост каждого ученика 
# и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). 
# Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

N = int(input('enter the number of students up to 100: '))
list = []
for i in range(N):
    list.append(int(input("enter the student's height from 120 to 180, less than the previous student: ")))
print(list)
H = int(input("enter Petya's height from 120 to 180: "))
place = 0
for y in range(N):
    if H > list[y]:
        list.insert(y, H)
        place = y + 1
        break
print(list)
print(f'the place in the line that Petya needs to stand on: {place}')
