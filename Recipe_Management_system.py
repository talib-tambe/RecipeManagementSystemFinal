import random




class Recipe:

    def __init__(self, id, name, ingredients, instructions, category, rating):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.rating = rating


class RecipeManager:

    def __init__(self):
        self.recipes = []
        self.id = []
        self.filtered_list = []

    def view_recipe_list(self, alist):
        for item in alist:
            print("ID : ", item.id)
            print("Name : ", item.name)
            print("Ingredients : ", item.ingredients)
            print("Instructions : ", item.instructions)
            print("Category : ", item.category)
            print("Rating : ", item.rating)
            print("\n")

    def view_recipe(self):

        if len(self.recipes) == 0:
            raise Exception("Recipe list empty!")

        print("\n")
        print("How do you wan to view the recipes as?")
        print("1. Full List")
        print("2. By Ratings")
        print("3. By Category")
        print("4. By Recipe name")
        filtered_choice = input("Enter Your Choice: ").lower()
        print("\n")

        if filtered_choice == "1":
            if len(self.recipes) == 0:
                raise Exception("Recipe List Empty")
            print("The list of recipes are:")
            self.view_recipe_list(self.recipes)
            return self.recipes

        elif filtered_choice == "2":
            self.filtered_list = []
            rating = input("Enter the rating : ").lower()
            print("\n")
            for item in self.recipes:
                if item.rating == rating:
                    self.filtered_list.append(item)
            if len(self.filtered_list) == 0:
                raise Exception("No Ratings of your choice found")
            print("The list of recipes are:")
            self.view_recipe_list(self.filtered_list)

        elif filtered_choice == "3":
            self.filtered_list = []
            category = input("Enter the category : ").lower()
            print("\n")
            for item in self.recipes:
                if item.category == category:
                    self.filtered_list.append(item)
            if len(self.filtered_list) == 0:
                raise Exception("No category of your choice found")
            print("The list of recipes are:")
            self.view_recipe_list(self.filtered_list)

        elif filtered_choice == "4":
            self.filtered_list = []
            name = input("Enter the receipe name : ").lower()
            print("\n")
            for item in self.recipes:
                if item.name == name:
                    self.filtered_list.append(item)
            print("The list of recipes are:")
            if len(self.filtered_list) == 0:
                raise Exception("No name of your choice found")
            print("The list of recipes are:")
            self.view_recipe_list(self.filtered_list)
        else:
            raise Exception("Choice Doesnt Exist")
        return self.filtered_list