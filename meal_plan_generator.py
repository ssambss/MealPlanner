from recipe import Recipe
from meal_plan import MealPlan

class MealPlanGenerator:
    def __init__(self, recipes):
        self.recipes = [Recipe(**recipe) for recipe in recipes]

    def generate_meal_plan(self):
        meal_plan = MealPlan()
        # Add logic to generate meal plan using self.recipes
        # and add them to meal_plan
        return meal_plan