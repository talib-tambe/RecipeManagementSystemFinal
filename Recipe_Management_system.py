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

    def add_recipe(self):

        random_id = random.randint(0, 500)
        while True:
            if random_id not in self.id:
                self.id.append(random_id)
                break
            random_id = random.randint(0, 500)

        name = input("Enter recipe name: ").lower()
        ingredients = input(
            "Enter the ingredients (with space after one another, no commas): ").lower()
        instructions = input(
            "Enter the instructions (with space after one another (numbered steps), no commas): ").lower()
        category = input("Enter recipe category: ").lower()
        rating = input("Enter recipe rating (1-5): ").lower()
        print("\n")

        if int(rating) < 1 or int(rating) > 5:
            raise Exception("Ratings must be between 1 and 5")

        if name == "" or ingredients == "" or instructions == "" or category == "" or rating == "":
            raise Exception("One of the entries are empty/missing")

        recipe = Recipe(random_id, name, ingredients,
                        instructions, category, rating)
        self.recipes.append(recipe)
        return True

    def edit_recipe(self):

        if len(self.recipes) == 0:
            raise Exception("Recipe list empty!")

        print("The list of recipes are:")
        self.view_recipe_list(self.recipes)
        print("\n")
        recipe_id = input(
            "Please enter the recipe id to which you want to modify: ")
        recipe = None
        recipe_index = None

        for item in self.recipes:
            if int(item.id) == int(recipe_id):
                recipe = item
                recipe_index = self.recipes.index(recipe)

        if recipe is None:
            raise Exception("Recipe doesnt exist")

        name = input("Enter recipe name: ").lower()
        ingredients = input(
            "Enter the ingredients (with space after one another): ").lower()
        instructions = input(
            "Enter the instructions (with space after one another): ").lower()
        category = input("Enter recipe category: ").lower()
        rating = input("Enter recipe rating (1-5): ").lower()

        updated_recipe = Recipe(
            item.id, name, ingredients, instructions, category, rating)
        self.recipes.append(updated_recipe)
        del self.recipes[recipe_index]
        return True

 def delete_recipe(self):

        if len(self.recipes) == 0:
            raise Exception("Recipe list empty!")

        print("The list of recipes are:")
        self.view_recipe_list(self.recipes)
        print("\n")
        recipe_id = input(
            "Please enter the recipe id to which you want to delete: ")
        recipe = None
        recipe_index = None

        for item in self.recipes:
            if int(item.id) == int(recipe_id):
                recipe = item
                recipe_index = self.recipes.index(recipe)
        if recipe is None:
            raise Exception("Recipe doesnt exist")
        del self.recipes[recipe_index]
        return True

    def export_data(self, file_format='csv'):
        if file_format == 'csv':
            with open('new_recipes.csv', 'w', newline='') as f:
                f.write('id,name,ingredients,instructions,category,rating\n')
                for recipe in self.recipes:
                    f.write(str(recipe.id)+","+recipe.name+","+recipe.ingredients+"," +
                            recipe.instructions+","+recipe.category+","+str(recipe.rating)+"\n")
        else:
            raise Exception("Only CSV files are supported")