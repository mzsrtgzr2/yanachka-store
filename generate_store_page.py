import json
import urllib.request


with open('./items.json', 'r') as fp:
    items = json.load(fp)

with open('README.md', 'w') as fp:
    for item in items:
        title = item.get('name')
        print('processing item', title)
        description = item.get('description')
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