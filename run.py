from pyecwid import Ecwid
import json
ecwid = Ecwid('xxx', '35000153')

# Get all products and use lambda function to search results
items = ecwid.products.get()
print(json.dumps(items))




