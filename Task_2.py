# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    """
    Функция для нахождения общих участников в двух группах.

    :param group1: строка участников первой группы, разделенных separator
    :param group2: строка участников второй группы, разделенных separator
    :param separator: разделитель участников в строке (по умолчанию ',')
    :return: список общих участников, отсортированный в алфавитном порядке
    """
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common = sorted(participants1 & participants2)
    return common

# Пример использования
group1 = "Иванов,Петров,Сидоров,Кузнецов"
group2 = "Петров,Кузнецов,Смирнов,Иванов"

common_participants = find_common_participants(group1, group2)
print(f"Общие участники: {common_participants}")
