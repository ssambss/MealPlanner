class MealPlan:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes
    
    def delete_recipe(self, recipe):
        self.recipes.remove(recipe)

    def update_recipe(self, recipe, new_recipe):
        self.recipes[self.recipes.index(recipe)] = new_recipe