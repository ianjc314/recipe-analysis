import requests
import xml.etree.ElementTree as ET

sitemap_url = 'https://www.allrecipes.com/sitemap.xml'
namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Get sitemap urls
try:
    response = requests.get(sitemap_url)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    sitemap_urls = []
    for sitemap in root.findall('ns:sitemap', namespace):
        loc = sitemap   .find('ns:loc', namespace)
        if loc is not None:
            sitemap_urls.append(loc.text)
except Exception as e:
    print(e)

# Get recipe urls
recipe_urls = []
for url in sitemap_urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        
        for sitemap in root.findall('ns:url', namespace):
            loc = sitemap.find('ns:loc', namespace)
            if loc is not None:
                if 'allrecipes.com/recipe/' in loc.text:
                    recipe_urls.append(loc.text)
    except Exception as e:
        print(e)

with open('generated_data/recipe_urls.txt', 'w') as f:
    for url in recipe_urls:
        f.write(url + '\n')