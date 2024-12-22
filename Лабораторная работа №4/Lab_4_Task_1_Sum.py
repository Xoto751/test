# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        json_data = json.load(f)
        results = 0
        for value in json_data:
            results += value['score'] * value['weight']
    return round(results, 3)



print(task())
