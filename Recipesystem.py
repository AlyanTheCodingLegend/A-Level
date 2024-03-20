import tkinter as tk
from tkinter import simpledialog, messagebox

# Class representing an ingredient
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    # Getter method for name
    def getName(self):
        return self.name

    # Getter method for quantity
    def getQuantity(self):
        return self.quantity

    # Getter method for unit
    def getUnit(self):
        return self.unit

# Class representing a recipe
class Recipe:
    def __init__(self, name):
        self.recipeName = name
        self.ingredients = []
        self.cookingInstructions = []

    # Method to add an ingredient to the recipe
    def addIngredient(self, ingredientName, ingredientQuantity, ingredientUnit):
        ingredient = Ingredient(ingredientName, ingredientQuantity, ingredientUnit)
        self.ingredients.append(ingredient)

    # Method to add a cooking instruction to the recipe
    def addCookingInstruction(self, instruction):
        self.cookingInstructions.append(instruction)

    # Method to display recipe details
    def displayRecipeDetails(self):
        details = "Recipe Name: {}\n".format(self.recipeName)
        details += "Ingredients:\n"
        for ingredient in self.ingredients:
            details += "- {} {} {}\n".format(ingredient.getName(), ingredient.getQuantity(), ingredient.getUnit())
        details += "Cooking Instructions:\n"
        for i, instruction in enumerate(self.cookingInstructions, start=1):
            details += "{}. {}\n".format(i, instruction)
        # Show recipe details in a message dialog
        messagebox.showinfo("Recipe Details", details)

# Main class for Recipe Management System
class RecipeManagementSystem:
    def __init__(self):
        self.recipes = []

    def run(self):
        while True:
            # Display menu options
            option = simpledialog.askstring("Menu", 
                "1. Create a new recipe.\n"
                "2. Add ingredients to a recipe.\n"
                "3. Add cooking instructions to a recipe.\n"
                "4. Display recipe details.\n"
                "5. Exit the program.\n"
                "Enter your choice:")

            # Switch based on user's choice
            if option == "1":
                recipeName = simpledialog.askstring("New Recipe", "Enter recipe name:")
                recipe = Recipe(recipeName)
                self.recipes.append(recipe)
            elif option == "2":
                recipeIndex = int(simpledialog.askstring("Add Ingredients", "Enter recipe index:")) - 1
                if 0 <= recipeIndex < len(self.recipes):
                    ingredientName = simpledialog.askstring("Ingredient Details", "Enter ingredient name:")
                    ingredientQuantity = int(simpledialog.askstring("Ingredient Details", "Enter ingredient quantity:"))
                    ingredientUnit = simpledialog.askstring("Ingredient Details", "Enter ingredient unit:")
                    self.recipes[recipeIndex].addIngredient(ingredientName, ingredientQuantity, ingredientUnit)
                else:
                    messagebox.showerror("Error", "Invalid recipe index.")
            elif option == "3":
                recipeIndex = int(simpledialog.askstring("Add Instructions", "Enter recipe index:")) - 1
                if 0 <= recipeIndex < len(self.recipes):
                    instruction = simpledialog.askstring("Add Instructions", "Enter cooking instruction:")
                    self.recipes[recipeIndex].addCookingInstruction(instruction)
                else:
                    messagebox.showerror("Error", "Invalid recipe index.")
            elif option == "4":
                recipeIndex = int(simpledialog.askstring("Display Recipe Details", "Enter recipe index:")) - 1
                if 0 <= recipeIndex < len(self.recipes):
                    self.recipes[recipeIndex].displayRecipeDetails()
                else:
                    messagebox.showerror("Error", "Invalid recipe index.")
            elif option == "5":
                break
            else:
                # Show message for invalid option
                messagebox.showerror("Error", "Invalid option. Please choose again.")

if __name__ == "__main__":
    app = RecipeManagementSystem()
    app.run()
