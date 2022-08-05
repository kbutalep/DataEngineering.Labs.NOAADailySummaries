import pandas as pd
import os
import json

file_path = os.path.join('./', 'data', 'daily_summaries')

def read_json(file_path):
    with open(file_path, 'r') as f:
        json_obj = json.load(f)
        return json_obj

def read_all_json_files(JSON_ROOT):
    df = pd.DataFrame()
    ser = pd.Series()
    for file_name in os.listdir(JSON_ROOT):
        if file_name.find('daily_summaries') == -1:
            continue
        file_path = 'data/daily_summaries/' + file_name
        data = read_json(file_path)
        for obj in data['results']:
            obj['source'] = file_name
        df = df.append(data['results'])
    return df

