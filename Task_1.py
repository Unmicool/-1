# TODO Напишите функцию для поиска индекса товара
def find_item_index(items_list, item_to_find):
    """
    Функция для поиска индекса первого вхождения товара в списке.

    :param items_list: список товаров
    :param item_to_find: товар, который нужно найти
    :return: индекс первого вхождения товара или None, если товар не найден
    """
    try:
        return items_list.index(item_to_find)
    except ValueError:
        return None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Поиск товаров в списке
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
