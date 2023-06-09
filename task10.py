# Задача 10: На столе лежат n монеток. Некоторые из них лежат 
# вверх решкой, а некоторые – гербом. Определите минимальное число 
# монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть. Стороны монеты 
# вводятся построчно или в одну строку, если умеете.

# Пример
# Ввод: 1 1 0 0 0 -> Вывод: 2

num_coins = int(input("Сколько монет: "))
tails = 0
for i in range(num_coins):
    if input('Сторона монетки: ') == '0':
        tails += 1
if tails > num_coins - tails:
    print(num_coins - tails)
else:
    print(tails)

coins = input().split() #split разделяет список и разделяет на символы
heads = coins.count('1') #count считает количество вхождений в список 
tails = coins.count('0')
print(f"минимальное колличество монет, которые\
нужно перевернуть: {min(heads, tails)}")