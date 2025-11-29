from recipe_scrapers import scrape_me
import csv

def safe_get(func):
    try:
        return str(func())
    except Exception:
        return ''

with open('generated_data/recipe_urls.txt', 'r') as f:
    recipe_urls = [line.strip() for line in f.readlines()]

f = open('generated_data/recipes.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow([
    'title',
    'canonical_url',
    'category',
    'cook_time',
    'cooking_method',
    'cuisine',
    'ingredients',
    'nutrients',
    'prep_time',
    'total_time',
    'site_name',
    'yields'])
f.close()

for i, url in enumerate(recipe_urls):
    scraper = scrape_me(url)

    values = [
        safe_get(scraper.title),
        safe_get(scraper.canonical_url),
        safe_get(scraper.category),
        safe_get(scraper.cook_time),
        safe_get(scraper.cooking_method),
        safe_get(scraper.cuisine),
        safe_get(scraper.ingredients),
        safe_get(scraper.nutrients),
        safe_get(scraper.prep_time),
        safe_get(scraper.total_time),
        safe_get(scraper.site_name),
        safe_get(scraper.yields)
    ]

    f = open('generated_data/recipes.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(values)
    f.close()