"""
Title: Pete, the baker
Source: https://www.codewars.com/kata/525c65e51bf619685c000059/python
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help
 him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns
 the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
 (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
  can be considered as 0.
Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


def cakes(recipe, available):

    listaDivInteira = []
    disponivel = {}

    if len(recipe) > len(available):        
        return 0

    for k in recipe.keys():                 
        if k not in available:
            return 0

    for k, v in available.items():         
        if k in recipe:
            disponivel[k] = v

    for k in disponivel.keys():
        listaDivInteira.append(disponivel[k] // recipe[k])
    return min(listaDivInteira)


#MAIN
print(cakes({'sugar': 67, 'apples': 38, 'nuts': 32}, {'cream': 6080, 'chocolate': 9862, 'apples': 8870, 'crumbles': 6407, 'butter': 4885, 'milk': 2759, 'cocoa': 3718, 'pears': 2170, 'eggs': 4371, 'flour': 8459}))
