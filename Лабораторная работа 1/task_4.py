users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
total_count_users = len(users)
unique_users = set(users)
count_unique_users = len(unique_users)
dictionary = { "Общее количество": 0 , "Уникальные посещения": 0 }
dictionary["Общее количество"] = total_count_users
dictionary["Уникальные посещения"] = count_unique_users
print(dictionary)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
