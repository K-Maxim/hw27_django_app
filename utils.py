import csv
import json

ads_scv = r'./datasets/ads.csv'
categories_scv = r'./datasets/categories.csv'
ads_model = 'ads.ad'

ads_json = r'./ads/fixtures/ads.json'
categories_json = r'./ads/fixtures/categories.json'
categories_model = 'ads.category'


def csv_to_json(csv_file, json_file, model):
    """cvs to json"""
    data = []

    with open(csv_file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            data.append({
                'model': model,
                'pk': int(row['id']) if row.get('id') else int(row['Id']),
                'fields': {
                    key: replace_value(values) for key, values in row.items() if key != 'id' and key != 'Id'
                }
            })
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))


def replace_value(values):
    if values.isdigit():
        return int(values)
    if values == "FALSE" or values == "TRUE":
        return bool(values)
    return values


csv_to_json(ads_scv, ads_json, ads_model)
csv_to_json(categories_scv, categories_json, categories_model)



