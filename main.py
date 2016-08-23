# Программа попытается угадать число загаданное вами от 1 до 100
# версия 2.0 (c GUI)
#==============================================
# подключение генератора чисел и GUI
import random
import easygui
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

easygui.msgbox("""\t\tЗдравствуйте!\n\
Сейчас вам необходимо загадать число от 1 до 100\n\
            Как только будите готовы нажмите кнопку""", ok_button="Я готов(а)!", image="sushi15.png")
count = 1
predpolozenie, predpolozenie2 = 1, 100
number = random.randint(predpolozenie, predpolozenie2)
vernost = easygui.ynbox("Я предпологаю, что вы загадали число: " + str(number) + "\n\t \
        Число верно?", choices=("[<F1>]да","[<F2>]нет"))
while not vernost:
    try:
        count += 1
        bolshe_or_not = easygui.buttonbox("Число больше или меньше загаданного?", choices=("больше","меньше"))
        if bolshe_or_not == "больше":
            predpolozenie2 = number - 1
        elif bolshe_or_not == "меньше":
            predpolozenie = number + 1
        number = random.randint(predpolozenie, predpolozenie2)
        vernost = easygui.ynbox("Хорошо. Теперь я думаю, что ваше число: " + str(number) + "\n\t \
        Число верно?", choices=("[<F1>]да","[<F2>]нет"))
    except ValueError:
        easygui.msgbox("Вы пытались обмануть программу! :)")
        predpolozenie, predpolozenie2 = 1, 100
        number = random.randint(predpolozenie, predpolozenie2)
        easygui.msgbox("Я предпологаю, что вы загадали число: " + str(number))
        continue

sklonenie()
# выводим результат
easygui.msgbox("Я угадал число " + str(number) + " за " + count, image="heart.png")
