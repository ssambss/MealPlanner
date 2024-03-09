from meal_plan_generator import MealPlanGenerator
from recipe import Recipe
import json

# Create a list of recipe objects from the recipes.json file
def createRecipeList():
    with open('Recipes/recipes.json', 'r') as f:
        recipes = json.load(f)

    recipeList = []

    for recipes in recipes['recipes']:
        recipeList.append(Recipe(recipes['name'], recipes['ingredients'], recipes['effort'], recipes['servings'], recipes['tags']))

    return recipeList

def main():

    mealPlan = generator.generate_meal_plan()

    # Write the generated meal plan to a text file
    with open('Meal Plan.txt', 'w') as f:
        f.write("Meal Plan:\n")
        f.write("\n")

        for recipe in mealPlan.get_recipes():
            f.write(recipe.get_name() + "\n")
        
        f.write("\n")
        f.write("Total Effort: " + str(sum([recipe.get_effort() for recipe in mealPlan.get_recipes()])) + "\n")
        f.write("Total Servings: " + str(sum([recipe.get_servings() for recipe in mealPlan.get_recipes()])) + "\n")
        f.write("Total Weekend Recipes: " + str(len([recipe for recipe in mealPlan.get_recipes() if "viikonloppu" in recipe.get_tags()])) + "\n")
    


recipeList = createRecipeList()

generator = MealPlanGenerator(recipeList, 10, 2)

if __name__ == "__main__":
    main()