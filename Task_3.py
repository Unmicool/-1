list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

# Разделение списка на две команды
first_team = list_players[:middle_index]  # Игроки с начала списка до середины
second_team = list_players[middle_index:]  # Игроки от середины до конца списка

# Печать команд
print(first_team)
print(second_team)