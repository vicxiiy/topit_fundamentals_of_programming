### Задание 1. От исходного кода к байткоду
#### Часть 1. Режимы запуска
`print(2 + 3 * 4)`

Результат в REPL отображается автоматически: 14 При запуске файла: ничего не выводится. После добавления `print()`: в терминале появляется 14.
#### Объяснение: 
В интерактивном режиме (REPL) интерпретатор Python автоматически выводит результат каждого выражения. При запуске файла как программы этот механизм отключен. Результат в терминале появляется только при вызове функции `print()`.

#### Часть 2. Выражения и инструкции
```
course = "Python"
hours = 4 * 2
print(f"{course}: {hours} часов")
```

Выражения:
• "Python" 
• 4 * 2 
• f"{course}: {hours} часов" 
• аргументы вызова print(...)
Инструкции:
• course = "Python" 
• hours = 4 * 2 
• print(...) 
Литералы:
"Python", 4, 2, ": ", " часов"
Имена, создаваемые при выполнении:
course, hours

#### Часть 3. AST и байткод
В AST нашлось:
1.	Присваивание: 
Assign(
   targets=[
      Name(id='course', ctx=Store())],
   value=Constant(value='Python'))
2.	Арифметическая операция:  
Assign(
   targets=[
      Name(id='hours', ctx=Store())],
   value=BinOp(
      left=Constant(value=4),
      op=Mult(),
      right=Constant(value=2)))
3.	Вызов print():
Expr(
   value=Call(
      func=Name(id='print', ctx=Load()),
      args=[
         JoinedStr(…)])
Фрагмент байткода:
             …
5           LOAD_CONST               1 ('Python')
            STORE_NAME               1 (course)

6           LOAD_SMALL_INT           8
            STORE_NAME               2 (hours)

7           LOAD_NAME                0 (print)
            PUSH_NULL
            LOAD_NAME                1 (course)
            FORMAT_SIMPLE
            LOAD_CONST               2 (': ')
            LOAD_NAME                2 (hours)
            FORMAT_SIMPLE
            LOAD_CONST               3 (' часов')
            BUILD_STRING             4
            CALL                     1
            POP_TOP
            LOAD_CONST               4 (None)
             …

В байткоде за загрузку константы отвечает LOAD_CONST, а за вызов функции - CALL.
### Контрольный вопрос:
Почему байткод CPython нельзя считать машинным кодом процессора?
Байткод - это не то, что процессор способен выполнить напрямую. Его понимает и обрабатывает интерпретатор Python: он построчно читает байткод и уже сам даёт процессору команды, что делать. Машинный код, в отличие от байткода, жёстко привязан к архитектуре конкретного процессора - для разных процессоров он разный.















