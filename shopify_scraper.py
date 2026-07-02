import json
import csv 
import requests

stores = [
    "https://www.glossier.com/products.json",
    "https://www.allbirds.com/products.json",
    
]

for store_url in stores:
    all_products = []
    page = 1
    
    while True:
        url = f'{store_url}?page={page}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = json.loads(response.text)
        except requests.exceptions.RequestException as e:
            print(f'Failed to fetch from:{store_url}: {e}')
            break
        
        products = data.get('products', [])
        
        if not products:
            break
        
        for product in products:
            product_title = product.get('title', '')
            product_type = product.get('product_type', '')
            
            
            for variant in product.get('variants', []):
                variant_title = variant.get('title', '')
                price = variant.get('price', 0)
                

                images = product.get('images', [])
                if images:
                    image_url = images[0].get('src', '')
                else:
                    image_url = 'No Image'
                
                all_products.append({
                    'product_title': product_title,
                    'product_type': product_type,
                    'variant': variant_title,
                    'price': price,
                    'image_url': image_url
                })
        
        page += 1
    
    if all_products:
        store_name = store_url.split('//')[1].replace('www.', '').split('.')[0]
        file_name = f'{store_name}_product.csv'
        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['product_title', 'product_type', 'variant', 'price', 'image_url']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_products)
        print(f'{store_name} : {len(all_products)} products saved to: {file_name}') 
    else:
        print(f'No data found: {store_url}')