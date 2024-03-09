class Recipe:
    def __init__(self, name, ingredients, type):
        self.name = name
        self.ingredients = ingredients
        self.type = type

    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients
    
    def delete_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def update_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def update_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    



    

