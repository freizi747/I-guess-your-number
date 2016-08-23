# Программа попытается угадать число загаданное вами от 1 до 100
# Версия 1.0 (без GUI)
#==============================================
# Подключение генератора чисел
import random

# сколняем окончание попыток
def sklonenie():
 global count
 if count == 1:
     count = str(count) + " попытку!"
 elif 1 < count < 5:
     count = str(count) + " попытки!"
 else:
     count = str(count) + " попыток!"
 return count

input('''Здравствуйте! сейчас вам необходимо загадать число от 1 до 100,
как только будите готовы нажмите кнопку "Enter"''')
count = 1
predpolozenie, predpolozenie2 = 1, 100
number = random.randint(predpolozenie, predpolozenie2)
vernost = ""
print("Я предпологаю, что вы загадали число:", number)

while True:
 try:
     vernost = str(input("число верно?\n"))
     if not vernost:
         continue
     elif vernost == "да" or vernost == "верно":
         break
     bolshe_or_not = ""
     count += 1
     while bolshe_or_not != "больше" or bolshe_or_not != "меньше":
             bolshe_or_not = str(input("Число больше или меньше загаданного?\n"))
             if bolshe_or_not == "больше":
                 predpolozenie2 = number - 1
             elif bolshe_or_not == "меньше":
                 predpolozenie = number + 1
             number = random.randint(predpolozenie, predpolozenie2)
             print("Хорошо. Теперь я думаю, что ваше число:", number)
             vernost = ""
             break
 except ValueError:
     print("Вы пытались обмануть программу! :)")
     predpolozenie, predpolozenie2 = 1, 100
     number = random.randint(predpolozenie, predpolozenie2)
     print("Я предпологаю, что вы загадали число:", number)
     continue

sklonenie()
# выводим результат
input("Я угадал число " + str(number) + " за " + count)
