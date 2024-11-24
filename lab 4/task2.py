import json

INPUT_FILENAME = "input.json"

def task() -> float:
    total_sum = 0.0

    # Открытие JSON файла и чтение содержимого
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)  # Загружаем данные из JSON файла

        # Итерация по всем объектам в загруженных данных
        for item in data:
            if 'score' in item and 'weight' in item:  # Чекаем наличие ключей
                # Вычисляем произведение score и weight и добавляем к общей сумме
                total_sum += item['score'] * item['weight']

    return round(total_sum, 3)  # Возвращаем сумму, округленную до 3 знаков после ,

if __name__ == '__main__':
    print(task())
