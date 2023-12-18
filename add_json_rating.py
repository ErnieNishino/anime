import json

# 请替换为你的文件路径
json_file_path = 'anime_data.json'

# 读取 JSON 文件
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    anime_data = json.load(json_file)

# 检测并添加 douban_ratings
for anime in anime_data:
    if 'douban_ratings' not in anime:
        anime['douban_ratings'] = '暂无人评分'

# 将更新后的数据写回 JSON 文件
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(anime_data, json_file, ensure_ascii=False, indent=2)

print(f'Douban Ratings have been successfully added to {json_file_path}')
