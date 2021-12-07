import json
import urllib.request
import re

with open('./items.json', 'r') as fp:
    items = json.load(fp)

with open('README.md', 'w') as fp:
    fp.write('<link rel="shortcut icon" type="image/png" href="assets/icon.png"><link rel="icon" type="image/png" href="assets/icon.png">\n')
    for item in items:
        title = item.get('name')
        fp.write(f'[ {title} ](#{title})&nbsp;')

    for item in items:
        title = item.get('name')
        print('processing item', title)
        description = item.get('description')
        # if description:
            # description = re.sub(r'<p>(.*?)</p>', r'<br>\1', description, re.UNICODE)
            # description = description.replace('<br/>', '\n')
            # description = description.replace('<br>', '\n')
            # description = re.sub(r'<strong>(.*?)</strong>', r'\n**\1**', description, re.UNICODE)
            # description = re.sub(r'<u>(.*?)</u>', r'\n*\1*', description, re.UNICODE)
        image_to_download = item.get('imageUrl')
        price = item.get('defaultDisplayedPriceFormatted')

        image_name = image_to_download.split('/')[-1]
        local_image = f"assets/{image_name}"
        urllib.request.urlretrieve(image_to_download, local_image)


        product_text = f"""
<div dir="rtl">
<a name="{title}"></a>
<h2>{title} - {price}</h2>

<img src="{local_image}" style="max-height:300px;"/>
<p>
{description}
</p>
<br>
</div>
"""
        fp.write(product_text + '<br/>')