import pandas as pd
import json

# 读取 Excel 文件
excel_file_path = 'anime_data.xlsx'
df = pd.read_excel(excel_file_path)

# 将数据转换为 JSON 格式
json_data = []

for index, row in df.iterrows():
    anime_data = {
        'name': row['片名'],
        'updateDay': row['更新时间'],
        'type': row['类型'],
        'introduction': row['简介'],
        'actors': row['演职人员'],
        'production': row['制作信息']
    }
    json_data.append(anime_data)

# 将数据保存到 JSON 文件
json_file_path = 'anime_data.json'  # 请替换为实际的 JSON 文件路径
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f'Data has been successfully converted to {json_file_path}')
