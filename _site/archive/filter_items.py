import json

with open('items.json', 'r') as fp:
    items = json.load(fp)

items_slim = [{
    'name': item.get('name'), 
    'description': item.get('description'), 
    'imageUrl': f"assets/images/{item['imageUrl'].split('/')[-1]}", 
    'defaultDisplayedPriceFormatted': item.get('defaultDisplayedPriceFormatted')} 
    for item in items]

with open('items.json', 'w', encoding='utf8') as json_file:
   json.dump(items_slim, json_file,  ensure_ascii=False)