# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    """
    Конвертирует содержимое CSV-файла в JSON и сохраняет результат в файл.
    """
    # Чтение содержимого CSV-файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)  # Используем DictReader для автоматического сопоставления столбцов и значений
        data = [row for row in reader]  # Преобразуем в список словарей

    # Сохранение в JSON с отступами
    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Запуск основной функции
    task()

    # Проверка: читаем и печатаем содержимое выходного файла
    with open(OUTPUT_FILENAME, mode="r", encoding="utf-8") as output_file:
        for line in output_file:
            print(line, end="")
