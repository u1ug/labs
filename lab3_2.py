# TODO Напишите функцию find_common_participants

def find_common_participants(group1_str: str, group2_str: str, sep: str = ',') -> list[str]:
    group1 = set(group1_str.split(sep))
    group2 = set(group2_str.split(sep))
    common = list(group1.intersection(group2))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))

# TODO Провеьте работу функции с разделителем отличным от запятой

participants_first_group = "Иванов;Петров;Сидоров"
participants_second_group = "Петров;Сидоров;Смирнов"

print(find_common_participants(participants_first_group,participants_second_group, sep=';'))
