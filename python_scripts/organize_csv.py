import pandas as pd
import ast
import re

df = pd.read_csv('generated_data/recipes.csv')

full_ingredients = []
for _, value in df['ingredients'].items():
    full_ingredients += ast.literal_eval(value)

ingredients_list = []

for text in full_ingredients:
    quantity_regex = '^[0-9.-/]+\\s*(\\([a-zA-Z0-9 .-/]*\\)\\s*)?'
    quantity_regex += '(cups?|teaspoons?|tsp|tbs|tablespoons?|oz|ounces?|g|grams?|ml|'
    quantity_regex += 'milliliters?|lb|pounds?|pinch(es)?|(thin\\s*)?slices?d?|cloves?|'
    quantity_regex += 'containers?|packages?|bags?|large|small|medium|cans?|dash(es)?|jars?)?'
    quantity_regex = '^(' + quantity_regex + ')+'

    quantity_match = re.search(quantity_regex, text)
    if quantity_match:
        quantity_str = quantity_match.group().strip()

    ingredient_str = [text.replace(quantity_str, '').strip(), '']

    replace_pairs = {
        'eggs': 'egg'
    }

    if ingredient_str[0] in replace_pairs:
        ingredient_str[0] = replace_pairs[ingredient_str[0]]
    
    ingredients_list.append([text, quantity_str] + ingredient_str)

ingredients_df = pd.DataFrame(ingredients_list, columns=[
    'full',
    'quantity',
    'ingredient_cleaned',
    'ingredient_detail'
])

pd.set_option('display.max_rows', None)
print(ingredients_df['ingredient_cleaned'].value_counts().head(100))