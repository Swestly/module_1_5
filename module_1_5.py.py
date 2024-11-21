def task_1() -> None:
    immutable_var = (1, 2, 3, "TEXT", "TWO TEXT", 3.14, True, [1, 2, 3])
    print(immutable_var)
    try:
        immutable_var[0] = 20
    except TypeError as e:
        print(f"Ошибка: {e}")
        if type(immutable_var) == tuple:
            print('Error')
# Кортежи в Python являются неизменяемыми (immutable) структурами данных.
# Это означает, что после создания кортежа его элементы не могут быть изменены. Попытка изменить элемент кортежа приводит к ошибке
# создания кортежа его элементы не могут быть изменены. Попытка изменить элемент кортежа приводит к ошибке.
# TypeError.
def task_2() -> None:
    mutable_list = [1, 2, 3, "Учиться", "Учиться", "И снова учиться", 5.6, False]
    print(mutable_list)
    mutable_list[3] = "не учиться"
    mutable_list[5] = "Учиться"
    print(mutable_list)
if __name__ == "__main__":
    task_1()
    task_2()