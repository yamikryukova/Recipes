from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipes(request, recipe: str):
    servings = int(request.GET.get("servings", 1))
    ingredients = DATA.get(recipe)
    if ingredients:
        ingredients = {
            ingredient: count * servings
            for ingredient, count in ingredients.items()
        }
    return render(request, "calculator/index.html", context={
        "recipe": ingredients
    })
