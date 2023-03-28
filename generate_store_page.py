import json
import re

with open('./items.json', 'r') as fp:
    items = json.load(fp)


for ii, item in enumerate(items):
    title = item.get('name')
    description = item.get('description', '') or ''
    image = item.get('imageUrl')
    price = item.get('defaultDisplayedPriceFormatted')
    
    description = description.replace('</p><p>', '. ').replace('<p>', '').replace('</p>', '')
    
    with open(f'./_posts/2023-03-27-{ii}.md', 'w') as fp:
        fp.write(f'''---
layout: post
title:  {title}
categories: [ all ]
author: yana
image: {image}
beforetoc: 
toc: true
price: {price}
---
{description}

<p><u>שימו לב:</u></p>
<p>- התשלום בפייבוקס או מזומן</p>
<p>- ינה סורגת את הבובות במיוחד אז הכנת הבובה תיקח בין שבוע לשבועיים<br></p>
<p>- לבקשות מיוחדות נא לפנות ישירות לינה בטלפון <a href="tel:0546405208" target="_blank">0546405208</a> או ב<a href="https://wa.me/972546405208?text=שלום, בקשר ל{title} נראה מעניין מאוד" target="_blank">ווטסאפ</a></p>
''')

# with open('README.md', 'w') as fp:
#     fp.write('<link rel="shortcut icon" type="image/png" href="assets/icon.png"><link rel="icon" type="image/png" href="assets/icon.png">\n')
#     for item in items:
#         title = item.get('name')
#         fp.write(f'[ {title} ](#{title})&nbsp;')

#     for item in items:
#         title = item.get('name')
#         print('processing item', title)
#         description = item.get('description', '') or ''
#         # if description:
#             # description = re.sub(r'<p>(.*?)</p>', r'<br>\1', description, re.UNICODE)
#             # description = description.replace('<br/>', '\n')
#             # description = description.replace('<br>', '\n')
#             # description = re.sub(r'<strong>(.*?)</strong>', r'\n**\1**', description, re.UNICODE)
#             # description = re.sub(r'<u>(.*?)</u>', r'\n*\1*', description, re.UNICODE)
#         local_image = item.get('imageUrl')
#         price = item.get('defaultDisplayedPriceFormatted')

#         product_text = f"""
# <div dir="rtl">
# <a name="{title}"></a>
# <h2>{title} - {price}</h2>

# <img src="{local_image}" style="max-height:300px;"/>
# <p>
# {description}
# </p>
# <br>
# </div>
# """
#         fp.write(product_text + '<br/>')