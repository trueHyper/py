
def find_common_participants(group1, group2, separator=','):

    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    
    commonParticipants = participants1.intersection(participants2)

    return sorted(commonParticipants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем '|' и 'запятая'
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("common participants (|):", common_participants)

# Можно также проверить с разделителем запятая
participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_participants_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma, separator=',')
print("common participants (,):", common_participants_comma)
