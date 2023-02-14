# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например,
# на входе
# 1+9/3*7-4
# на выходе
# 18

def calculate(expr):
    # Убираем пробелы из выражения
    expr = expr.replace(' ', '')

    # Ищем самый вложенный парный оператор, чтобы сначала его вычислить
    level = 0
    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ')':
            level += 1
        elif expr[i] == '(':
            level -= 1
        elif level == 0 and expr[i] in '+-':
            # Если нашли + или -, значит, внутри скобок нет операторов с большим приоритетом
            # и можно рекурсивно вычислить левую и правую части выражения
            left = calculate(expr[:i])
            right = calculate(expr[i+1:])
            # Выполняем операцию и возвращаем результат
            if expr[i] == '+':
                return left + right
            else:
                return left - right

    # Если скобки не нашли, значит, ищем операторы с большим приоритетом (*/), иначе - просто число
    level = 0
    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ')':
            level += 1
        elif expr[i] == '(':
            level -= 1
        elif level == 0 and expr[i] in '*/':
            left = calculate(expr[:i])
            right = calculate(expr[i+1:])
            if expr[i] == '*':
                return left * right
            else:
                return left / right

    # Если осталось только одно число, просто его возвращаем
    return int(expr)

expr = input("Введите выражение: ")
result = calculate(expr)
print("Результат:", result)
