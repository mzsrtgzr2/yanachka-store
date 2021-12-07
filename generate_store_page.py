import json
import urllib.request
import re

with open('./items.json', 'r') as fp:
    items = json.load(fp)

with open('README.md', 'w') as fp:
    fp.write('# החנות של ינהצ׳קה\n')

    for item in items:
        title = item.get('name')
        print('processing item', title)
        description = item.get('description')
        if description:
            description = re.sub(r'<p>(.*?)</p>', r'\n\1', description, re.UNICODE)
            description = description.replace('<br/>', '\n')
            description = description.replace('<br>', '\n')
            description = re.sub(r'<strong>(.*?)</strong>', r'\n**\1**', description, re.UNICODE)
            description = re.sub(r'<u>(.*?)</u>', r'\n*\1*', description, re.UNICODE)
        print(description)
        image_to_download = item.get('imageUrl')

        image_name = image_to_download.split('/')[-1]
        local_image = f"assets/{image_name}"
        urllib.request.urlretrieve(image_to_download, local_image)


        product_text = f"""
## {title}
#### {description}
![]({local_image})
"""
        fp.write(product_text + '\n')