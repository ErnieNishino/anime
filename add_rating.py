import json
from crawler import get_douban_rating
# 文件路径
json_file_path = 'anime_data.json'

# 读取 JSON 文件
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    anime_data = json.load(json_file)

# 调用 get_douban_rating 函数获取豆瓣评分
for anime in anime_data:
    title = anime['name']
    douban_ratings = get_douban_rating(title)

    # 将豆瓣评分添加到数据中
    if douban_ratings:
        anime['douban_ratings'] = douban_ratings[0]  # 只取第一个评分
    else:
        anime['douban_ratings'] = "暂无人评分"

# 将更新后的数据写回 JSON 文件
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(anime_data, json_file, ensure_ascii=False, indent=2)

print(f'Douban Ratings have been successfully added to {json_file_path}')
