# TODO решите задачу
import json

def task() -> float:
    """
    Вычисляет сумму произведений значений 'score' и 'weight' для каждого словаря в JSON-файле.
    :return: Округленная до 3 знаков сумма произведений
    """
    # Путь к файлу с JSON-данными
    file_path = "input.json"

    # Чтение данных из JSON-файла
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Вычисление суммы произведений
    total = sum(item["score"] * item["weight"] for item in data)

    # Возвращаем округленное значение
    return round(total, 3)


# Вызов функции и вывод результата
print(task())
