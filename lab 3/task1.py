# TODO Напишите функцию для поиска индекса товара

def find_item_index(products, item):
    for index, product in enumerate(products):
        if product == item:
            return index
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    indexItem = find_item_index(items_list, find_item) 
    if indexItem is not None:
        print(f"first match '{find_item}' with index {indexItem}.")
    else:
        print(f"'{find_item}' not found.")
