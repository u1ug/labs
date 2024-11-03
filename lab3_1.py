# TODO Напишите функцию для поиска индекса товара

def item_index(item_list: list[str], target_item: str) -> int | None:
    for item_idx, item in enumerate(item_list):
        if item == target_item:
            return item_idx
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
