print('Бомба\n')

# Мы разрабатываем пошаговую игру по мотивам боевика.
# Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд.
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
#
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва..
#
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.

time_in_seconds = int(input('Введите количество секунд: '))

for number_person in range(0, time_in_seconds, 1):
  print('Хотите обезвредить бомбу сейчас?\n0 — нет\n1 — да')
  answer = int(input())
  if answer == 0:
    time_in_seconds -= 1
    if time_in_seconds != 0:
    print('До взрыва оставалось', time_in_seconds, 'секунд')
    continue
  elif answer == 1:
    print('Бомба обезврежена, до взрыва оставалось', time_in_seconds, 'секунд')
    break
  else:
    print('Ошибка! Введите 0 или 1')
    continue
  print('Бомба взорвалась')
