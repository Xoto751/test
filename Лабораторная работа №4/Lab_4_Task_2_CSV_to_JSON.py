# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding = 'utf-8') as f:
        csv_data = list(csv.DictReader(f, delimiter=',', quotechar='\n'))

    with open(OUTPUT_FILENAME, 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(csv_data, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
