from meal_plan import MealPlan
import random

class MealPlanGenerator:

    """

    This class is responsible for generating a meal plan based on a list of recipes and a set of constraints.
    
    """
    def __init__(self, recipes, maxEffort, maxWeekendRecipes=2, maxWeeklyServings=14):
        self.recipes = recipes
        self.maxEffort = maxEffort
        self.maxWeekendRecipes = maxWeekendRecipes
        self.maxWeeklyServings = maxWeeklyServings

    def generate_meal_plan(self):

        # Initialize constraint variables and an empty meal plan
        mealPlan = MealPlan()
        currentEffort = 0
        currentWeekendRecipes = 0
        currentServings = 0
        random.shuffle(self.recipes)


        # Add recipes to the meal plan until the effort, weekend recipes, and weekly servings constraints are met
        for recipe in self.recipes:
            if currentEffort + recipe.get_effort() <= self.maxEffort and currentWeekendRecipes < self.maxWeekendRecipes and currentServings + recipe.get_servings() <= self.maxWeeklyServings:
                mealPlan.add_recipe(recipe)
                currentEffort += recipe.get_effort()
                currentServings += recipe.get_servings()
                if "viikonloppu" in recipe.get_tags():
                    currentWeekendRecipes += 1

        # Move the weekend recipes to the end of the meal plan
        for recipe in mealPlan.get_recipes():
            if "viikonloppu" in recipe.get_tags():
                mealPlan.recipes.append(mealPlan.recipes.pop(mealPlan.recipes.index(recipe)))

        return mealPlan

    