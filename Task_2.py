# Параметры
diskette_size_mb = 1.44  # Размер дискеты в Мб
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
chars_per_line = 25  # Количество символов в строке
bytes_per_char = 4  # Количество байт для хранения одного символа

# Рассчитаем объем одной книги в байтах
chars_per_book = pages_per_book * lines_per_page * chars_per_line  # Количество символов в книге
book_size_bytes = chars_per_book * bytes_per_char  # Объем книги в байтах

# Рассчитаем объем дискеты в байтах
diskette_size_bytes = diskette_size_mb * 1024 * 1024  # Объем дискеты в байтах

# Рассчитаем, сколько книг помещается на дискету
books_count = diskette_size_bytes // book_size_bytes  # Целочисленное деление

# Выводим результат
print("Количество книг, помещающихся на дискету:", int(books_count))
