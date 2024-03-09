class Recipe:

    """
    
    A base class for recipe objects.
    
    """

    def __init__(self, name, ingredients, effort, servings, tags=[]):
        self.name = name
        self.ingredients = ingredients
        self.effort = effort
        self.tags = tags
        self.servings = servings

    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients
    
    def delete_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def update_effort(self, effort):
        self.effort = effort

    def get_effort(self):
        return self.effort

    def update_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def update_tags(self, tags):
        self.tags = tags

    def get_tags(self):
        return self.tags
    
    def delete_tags(self, tag):
        self.tags.remove(tag)

    def update_servings(self, servings):
        self.servings = servings

    def get_servings(self):
        return self.servings
    


    

