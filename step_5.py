import sys

result = 0
while True:
    string = input("Введите номер или специальный жетон q для выхода: ")
    signs = string.split(" ")
    for sign in signs:
        try:
            number = float(sign)
            result += number
        except:
            if sign == 'q':
                print(f"Ваша сумма {result}. Программа прекращена")
                exit(0)
            else:
                print(f"Ваша сумма {result}. Ошибка ввода", file=sys.stderr)
                exit(1)
#print(result)
#exit()