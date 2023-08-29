import argparse
import json

def trim_text(data, amount=10000):
    data['actions_metadata'] = {}

    total_length = 0
    trimmed_actions = []

    for action in reversed(data['actions']):
        if total_length + len(action) <= amount:
            trimmed_actions.insert(0, action)
            total_length += len(action)
        else:
            break

    data['actions'] = trimmed_actions

    return data

def main():
    parser = argparse.ArgumentParser(description="Триммер для удаления ненужных данных из файлов сохранения KoboldAI")
    parser.add_argument('-i', '--input', help="Путь к входному файлу")
    parser.add_argument('-o', '--output', help="Путь для выходного файла")
    parser.add_argument('-v', '--version', action='store_true', help="Показать версию")
    parser.add_argument('-a', '--amount', type=int, help="Количество текста которое нужно сохранить. По умолчанию 10000")

    args = parser.parse_args()

    if args.version:
        print("Version: 1.2")
        return

    if not (args.input and args.output):
        parser.print_usage()
        return

    amount = args.amount if args.amount is not None else 10000

    with open(args.input, 'r', encoding='utf-8') as file:
        data = json.load(file)

    trimmed_data = trim_text(data, amount)

    with open(args.output, 'w', encoding='utf-8') as file:
        json.dump(trimmed_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
